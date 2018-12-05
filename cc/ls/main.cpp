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

string path_join(const string& base_dir, const string &file_name) {
    string res(base_dir);
    if (res[res.length() - 1] != '/') {
        res += '/';
    }
    res += file_name;
    return res;
}

struct FileEntry {
    string rel_name;
    string full_name;
    int mode;
    unsigned long nlink;
    char *user_name;
    char *group_name;
    long size;
    struct timespec time;
    
    FileEntry(const string& dir_name, const string& file_name) {
        string full_name = path_join(dir_name, file_name);
        struct stat stat_buf;
        // lstat do not dereference symbolic links
        if (lstat(full_name.c_str(), &stat_buf) == -1) {
            oops("cannot access file", full_name);
        }

        this->rel_name = file_name;
        this->full_name = full_name;
        this->mode = stat_buf.st_mode;
        this->nlink = stat_buf.st_nlink;
        this->user_name = getpwuid(stat_buf.st_uid)->pw_name;
        this->group_name = getgrgid(stat_buf.st_gid)->gr_name;
        this->size = stat_buf.st_size;
        this->time = stat_buf.st_mtim;
    }

    void print() const {
        printf("%s ", mode2str(mode).c_str());
        printf("%3lu ", nlink);
        printf("%s ", user_name);
        printf("%s ", group_name);
        printf("%8ld ", size);
        printf("%.12s ", ctime(&time.tv_sec) + 4);
        printf("%s\n", rel_name.c_str());
    }

    static string mode2str(int mode) {
        string mode_str("----------");
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
        return mode_str;
    }
};

void do_ls(const string &dir_name) {
    DIR *dir = opendir(dir_name.c_str());
    if (dir == nullptr) {
        fprintf(stderr, "ls: cannot open %s\n", dir_name.c_str());
    }

    struct dirent *ent;
    vector<FileEntry> file_entries;
    while ((ent = readdir(dir)) != nullptr) {
        string file_name(ent->d_name);
        // Ignore hidden files by default
        if (file_name[0] == '.') {
            continue;
        }
        FileEntry entry(dir_name, file_name);
        file_entries.push_back(entry);
    }
    closedir(dir);

    sort(file_entries.begin(), file_entries.end(), [](const FileEntry& one, const FileEntry& another) {
        return one.rel_name < another.rel_name;
    });

    for (const auto& fe : file_entries) {
        fe.print();
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