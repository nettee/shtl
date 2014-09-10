#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXLINE 1000

int main(int argc, char *argv[])
{
    char line[MAXLINE];
    long lineno = 0;
    char c;
    int except = 0, number = 0, found = 0;

    while (--argc > 0 && (*++argv)[0] == '-') {
        while ((c = *++argv[0])) {
            switch (c) {
            case 'x':
                except = 1;
                break;
            case 'n':
                number = 1;
                break;
            default:
                fprintf(stderr, "grep: illegal option %c\n", c);
                argc = 0;
                found = -1;
                break;
            }
        }
    }
    if (argc != 1) {
        fprintf(stderr, "usage: find -x -n pattern\n");
        exit(1);
    }
    while (fgets(line, MAXLINE, stdin) != NULL) {
        lineno++;
        if ((strstr(line, argv[0]) != NULL) != except) {
            if (number)
                printf("%ld:", lineno);
            fputs(line, stdout);
            found++;
        }
    }
    return 0;
}

