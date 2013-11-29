#include <stdio.h>

#define NTAB 8

int main(void)
{
    int c;
    int col = 0;
    while ((c = getchar()) != EOF) {
        if (c == '\n') {
            putchar('\n');
            col = 0;
            continue;
        }
        if (c == '\t') {
            for (int i = 0; i < NTAB - col; i++) {
                putchar(' ');
            }
        } else {
            putchar(c);
        }
        col = (col + 1) % NTAB;
    } 
}
