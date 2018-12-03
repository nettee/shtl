#include <stdio.h>
#include <stdlib.h>
#include <utmp.h>
#include <fcntl.h>
#include <unistd.h>

#define SHOWHOST

void show_info(struct utmp *prec) {
    printf("%-8.8s %-8.8s %10ld ", prec->ut_name, prec->ut_line, prec->ut_time);
#ifdef SHOWHOST
    printf("(%s)", prec->ut_host);
#endif
    printf("\n");
}

int main() {
    int utmp_fd = open(UTMP_FILE, O_RDONLY);
    if (utmp_fd == -1) {
        perror(UTMP_FILE);
        exit(1);
    }

    struct utmp rec;
    size_t rec_size = sizeof(rec);
    while (read(utmp_fd, &rec, rec_size) == rec_size) {
        show_info(&rec);
    }
    close(utmp_fd);

    return 0;
}