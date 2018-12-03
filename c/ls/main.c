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

char *path_join(const char *base_dir, const char *file_name) {
    size_t s1 = strlen(base_dir);
    size_t s2 = strlen(file_name);
    char *dest = malloc(s1 + s2 + 2);
    strcpy(dest, base_dir);
    char *p = dest + s1;
    if (p[-1] != '/') {
        *p++ = '/';
    }
    strcpy(p, file_name);
    return dest;
}

struct fileent {
    char *rel_name;
    char *full_name;
    int mode;
    unsigned long nlink;
    char *user_name;
    char *group_name;
    long size;
    struct timespec time;
};

void get_file_ent(char *rel_name, char *full_name, struct fileent *buf) {
    struct stat stat_buf;
    // lstat do not dereference symbolic links
    if (lstat(full_name, &stat_buf) == -1) {
        oops("cannot access file", full_name);
    }

    buf->rel_name = rel_name;
    buf->full_name = full_name;
    buf->mode = stat_buf.st_mode;
    buf->nlink = stat_buf.st_nlink;
    buf->user_name = getpwuid(stat_buf.st_uid)->pw_name;
    buf->group_name = getgrgid(stat_buf.st_gid)->gr_name;
    buf->size = stat_buf.st_size;
    buf->time = stat_buf.st_mtim;
}

void print_file_ent(struct fileent *file_ent) {
    char mode_str[11];
    mode2str(file_ent->mode, mode_str);
    printf("%s ", mode_str);
    printf("%3lu ", file_ent->nlink);
    printf("%s ", file_ent->user_name);
    printf("%s ", file_ent->group_name);
    printf("%8ld ", file_ent->size);
    printf("%.12s ", ctime(&file_ent->time.tv_sec) + 4);
    printf("%s\n", file_ent->rel_name);
}

void do_ls(char* dir_name) {
    DIR *dir = opendir(dir_name);
    if (dir == NULL) {
        fprintf(stderr, "ls: cannot open %s\n", dir_name);
    }

    struct dirent *ent;
    while ((ent = readdir(dir)) != NULL) {
        char *file_name = ent->d_name;
        if (file_name[0] == '.') {
            continue;
        }
        char *full_name = path_join(dir_name, file_name);
        struct fileent file_ent_buf;
        get_file_ent(file_name, full_name, &file_ent_buf);
        print_file_ent(&file_ent_buf);
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