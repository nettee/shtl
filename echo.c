#include <stdio.h>

/* not implemented yet
 * 2013-11-28
 */

void escape(char *s, char *t)
{
    while (*t != '\0') {
        if (*t == '\\') {
            ++t;
            switch (*t) {
            case 'n':
                *s++ = '\n';
                break;
            case 't':
                *s++ = '\t';
                break;
            default:
                *s++ = '\\';
                *s++ = *t;
                break;
            }
        } else {
            *s++ = *t++;
        }
    }
}

int main(int argc, char *argv[])
{
    
    return 0;
}
