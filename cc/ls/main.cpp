#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <memory.h>
#include <pwd.h>
#include <grp.h>
#include <time.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void oops(string s1, string s2) {
    fprintf(stderr, "Error: %s ", s1.c_str());
    perror(s2.c_str());
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

string path_join(const string& base_dir, const string &file_name) {
    string res(base_dir);
    if (res[res.length() - 1] != '/') {
        res += '/';
    }
    res += file_name;
    return res;
}

struct fileent {
    string rel_name;
    string full_name;
    int mode;
    unsigned long nlink;
    char *user_name;
    char *group_name;
    long size;
    struct timespec time;
};

void get_file_ent(const string& rel_name, const string& full_name, fileent *buf) {
    struct stat stat_buf;
    // lstat do not dereference symbolic links
    if (lstat(full_name.c_str(), &stat_buf) == -1) {
        oops("cannot access file", full_name.c_str());
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
    printf("%s\n", file_ent->rel_name.c_str());
}

void do_ls(const string &dir_name) {
    DIR *dir = opendir(dir_name.c_str());
    if (dir == nullptr) {
        fprintf(stderr, "ls: cannot open %s\n", dir_name.c_str());
    }

    struct dirent *ent;
    vector<fileent> file_entries;
    while ((ent = readdir(dir)) != nullptr) {
        string file_name(ent->d_name);
        if (file_name[0] == '.') {
            continue;
        }
        string full_name = path_join(dir_name, file_name);
        struct fileent file_ent;
        get_file_ent(file_name, full_name, &file_ent);
        file_entries.push_back(file_ent);
    }
    closedir(dir);

    sort(file_entries.begin(), file_entries.end(), [](const fileent& one, const fileent& another) {
        return one.rel_name < another.rel_name;
    });

    for (const auto& fe : file_entries) {
        cout << fe.rel_name << endl;
    }
}

int main(int argc, char *argv[]) {

    if (argc == 1) {
        do_ls(".");
    } else {
        int i;
        for (i = 1; i < argc; i++) {
            string dir_name(argv[i]);
            printf("%s:\n", dir_name.c_str());
            do_ls(dir_name);
        }
    }

    return 0;
}