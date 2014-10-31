/* double - find adjacent identical words
 * version 1.0.0
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <errno.h>

int linenum;

int getword(FILE *, char *, int);
void double_word(char *, FILE *);

int main(int argc, char *argv[]) {
    int i;
    for (i = 1; i < argc; i++) {
        FILE *fp = fopen(argv[i], "r");
        if (fp == NULL) {
            fprintf(stderr, "%s: %s: %s\n", argv[0], argv[i], strerror(errno));
            return 1;
        } else {
            double_word(argv[i], fp);
            fclose(fp);
        }
    }
    if (argc == 1) {
        double_word(NULL, stdin);
    }
    return 0;
}

void double_word(char *name, FILE *fp)
{
    char prev[128], word[128];
    linenum = 1;
    prev[0] = '\0';

    while (getword(fp, word, sizeof word)) {
        if (isalpha(word[0]) && strcmp(prev, word) == 0) {
            if (name) {
                printf("%s:", name);
            }
            printf("%d: %s\n", linenum, word);
        }
        strcpy(prev, word);
    }
}    

int getword(FILE *fp, char *buf, int size) 
{
    assert(buf != NULL);
    char c;
    int i = 0;
    c = getc(fp);
    /* scan forward to a nonspace charactor */
    for ( ; c != EOF && isspace(c); c = getc(fp)) {
        if (c == '\n') {
            linenum++;
        }
    }
    /* scan and copy a word into buf */
    for ( ; c != EOF && !isspace(c); c = getc(fp)) {
        if (i < size - 1) {
            buf[i++] = tolower(c);
        }
    }
    if (i < size) {
        buf[i] = '\0';
    }

    if (c != EOF) {
        ungetc(c, fp);
    }
    return buf[0] != '\0';
}
