#include <stdio.h>

#define NTAB 8
#define MAXLINE 1000

int main(void)
{
    char line[MAXLINE];
    char *p;
    while ((p = fgets(line, MAXLINE, stdin)) != NULL) {
        int col = 0;
        for ( ; *p != '\0'; p++) {
            if (*p == '\t') {
                for (int i = 0; i < NTAB - col; i++) {
                    putchar(' ');
                }
            } else {
                putchar(*p);
            }
            col = (col + 1) % NTAB;
        }
    }
}
