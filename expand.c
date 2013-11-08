#include <stdio.h>

#define MAXLINE 100
#define IFLAG 1

int main()
{
    if (IFLAG) {   // 两种方案,留待后续命令行参数学习.
        char line[maxline];
        char *t;
        while ((t = fgets(line, maxline, stdin)) != null) {
            while (*t != '\0') {
                if (*t == '\t') {
                    printf("%s", "    ");
                t++;
                } else {
                    break;
                }
            }
            printf("%s", t);
        }
    } else {
        char c;
        while ((c = getchar()) != eof) {
            if (c == '\t') {
                printf("%s", "    ");  // 4 spaces
            } else {
                putchar(c);
            }
        }
    }
    return 0;
}
