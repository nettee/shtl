#include <stdio.h>

#define NTAB 8
#define MAXLINE 1000

int main(void)
{
    char line[MAXLINE];
    char *p;
    while ((p = fgets(line, MAXLINE, stdin)) != NULL) {
        int nblank = 0;
        for (char *t = p; *t == ' '; t++)
            nblank++;
        int ntab = nblank / NTAB;
        for (int i = 0; i < ntab; i++)
            putchar('\t');

        nblank = nblank % NTAB;
        for (int i = 0; i < nblank; i++)
            putchar(' ');
    }
}
