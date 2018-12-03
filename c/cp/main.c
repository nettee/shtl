#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

#define BUFFER_SIZE 4096
#define COPY_MODE 0644

void oops(char *s1, char *s2) {
    fprintf(stderr, "Error: %s ", s1);
    perror(s2);
    exit(1);
}

int main(int argc, char *argv[]) {
    
    if (argc != 3) {
        fprintf(stderr, "usage: cp SOURCE DEST\n");
        exit(1);
    }

    char *in_filename = argv[1];
    int in_fd = open(in_filename, O_RDONLY);
    if (in_fd == -1) {
        oops("Cannot open", in_filename);
    }

    char *out_filename = argv[2];
    int out_fd = creat(out_filename, COPY_MODE);
    if (out_fd == -1) {
        oops("Cannot creat", out_filename);
    }
    
    char buf[BUFFER_SIZE];
    int n_chars;
    while ((n_chars = read(in_fd, buf, BUFFER_SIZE)) > 0) {
        if (write(out_fd, buf, n_chars) != n_chars) {
            oops("Write error to", out_filename);
        }
    }
    
    if (n_chars == -1) {
        oops("Read error from", in_filename);
    }
    
    if (close(in_fd) == -1 || close(out_fd) == -1) {
        oops("Error closing files", "");
    }
    
    return 0;
}