#include <stdio.h>

/* copy everything from input to output 
 */

int main()
{
    int c;
    while ((c = getchar()) != EOF) {
        putchar(c);
    }
    return 0;
}
