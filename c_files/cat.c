#include <stdio.h>
#include <errno.h>

/* cat - concatenate files,
 * version 0.0.3
 */

void filecopy(FILE *fin, FILE *fout)
{
    char c;
    while ((c = getc(fin)) != EOF) {
        putc(c, fout);
    }
}

int main(int argc, char *argv[])
{
    FILE *fp;
    int i;
    for (i = 1; i < argc; i++) {
        fp = fopen(argv[i], "r");
        if (fp == NULL) {
            fprintf(stderr, "%s: %s: %s\n", argv[0], argv[i], strerror(errno));
        } else {
            filecopy(fp, stdout);
            fclose(fp);
        }
    }
    if (argc == 1) {  /* copy standard input */
        filecopy(stdin, stdout);
    }
    return 0;
}
