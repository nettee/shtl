#include <stdio.h>

/* wc - count lines, words and characters in input
 * version: 0.1.0
 * 2013-11-28
 */

#define IN 1
#define OUT 0

int main()
{
    int c;
    int state = OUT;
    int nl = 0, nw = 0, nc = 0;

    while ((c = getchar()) != EOF) {
        ++nc;
        if (c == '\n')
            ++nl;
        if (c == ' ' || c == '\n' || c == '\t')
            state = OUT;
        else if (state == OUT) {
            state = IN;
            ++nw;
        }
    }
    printf("%3d %3d %3d\n", nl, nw, nc);
    
    return 0;
}
