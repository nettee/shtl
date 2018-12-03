#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <memory.h>
#include <pwd.h>
#include <grp.h>
#include <time.h>

void oops(char *s1, char *s2) {
    fprintf(stderr, "Error: %s ", s1);
    perror(s2);
    exit(1);
}

void mode2str(int mode, char *mode_str) {
    strcpy(mode_str, "----------");
    if (mode & S_IFDIR) mode_str[0] = 'd';
    if (mode & S_IRUSR) mode_str[1] = 'r';
    if (mode & S_IWUSR) mode_str[2] = 'w';
    if (mode & S_IXUSR) mode_str[3] = 'x';
    if (mode & S_IRGRP) mode_str[4] = 'r';
    if (mode & S_IWGRP) mode_str[5] = 'w';
    if (mode & S_IXGRP) mode_str[6] = 'x';
    if (mode & S_IROTH) mode_str[7] = 'r';
    if (mode & S_IWOTH) mode_str[8] = 'w';
    if (mode & S_IXOTH) mode_str[9] = 'x';
}

void do_stat(char *file_name) {
    struct stat stat_buf;
    // lstat do not dereference symbolic links
    if (lstat(file_name, &stat_buf) == -1) {
        oops("cannot access file", file_name);
    }

    char mode_str[11];
    mode2str(stat_buf.st_mode, mode_str);

    printf("%s ", mode_str);
    printf("%lu ", stat_buf.st_nlink);
    printf("%s ", getpwuid(stat_buf.st_uid)->pw_name);
    printf("%s ", getgrgid(stat_buf.st_gid)->gr_name);
    printf("%5ld ", stat_buf.st_size);
    printf("%.12s ", ctime(&stat_buf.st_mtim.tv_sec) + 4);
    printf("%s\n", file_name);
}

void do_ls(char dir_name[]) {
    DIR *dir = opendir(dir_name);
    if (dir == NULL) {
        fprintf(stderr, "ls: cannot open %s\n", dir_name);
    }

    struct dirent *ent;
    while ((ent = readdir(dir)) != NULL) {
        do_stat(ent->d_name);
    }
    closedir(dir);
}

int main(int argc, char *argv[]) {

    if (argc == 1) {
        do_ls(".");
    } else {
        int i;
        for (i = 1; i < argc; i++) {
            char *dir_name = argv[i];
            printf("%s:\n", dir_name);
            do_ls(dir_name);
        }
    }

    return 0;
}