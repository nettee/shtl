#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

#define PERMS 0644
#define BUFSIZE 32

int main(int argc, char *argv[])
{
    int f1, f2;
    char buf[BUFSIZE];
    int n;

    if (argc != 3) {
        fprintf(stderr, "Usage: cp from to\n");
        exit(1);
    }
    if ((f1 = open(argv[1], O_RDONLY, 0)) == -1) {
        fprintf(stderr, "cp: can't open %s\n", argv[1]);
        exit(1);
    }
    if ((f2 = creat(argv[2], PERMS)) == -1) {
        fprintf(stderr, "cp: can't create %s, mode %03o\n",
                argv[2], PERMS);
        exit(1);
    }
    while ((n = read(f1, buf, BUFSIZE)) > 0) {
        if (write(f2, buf, n) != n) {
            fprintf(stderr, "cp: write error on file %s\n",
                    argv[2]);
            exit(1);
        }
    }
    return 0;
}
