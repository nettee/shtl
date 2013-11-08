#!/usr/bin/python3.2

import sys

def cat(files):
    for each_file in files:
        with open(each_file, "r") as fobj:
            for line in fobj:
                print(line, end = '')

def main():
    files = sys.argv[1:]
    if(files):
        cat(files)
    else:
        print('usage: cat file1 [file2 ...]', file=sys.stderr)

if __name__ == '__main__':
    main()
