#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void cat(char *filename);

int main(int argc, char *argv[])
{
    string line;
    if (argc == 1) {
        // "-" indicates stdin
        cat("-");
    } else {
        for (int i = 1; i != argc; ++i) {
            cat(argv[i]);
        }
    }
    return 0;
}

void cat(char *filename)
{
    string line;
    // "-" indicates stdin
    if (filename == "-") {
        while (getline(cin, line)) {
            cout << line << endl;
        }
    } else {
        ifstream fin(filename);
        while (getline(fin, line)) {
            cout << line << endl;
        }
        fin.close();
    }
}
