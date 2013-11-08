#!/usr/bin/python3.2

import sys

def tac(files):
    for each_file in files:
        with open(each_file, "r") as fobj:
            for line in fobj.readlines[::-1]:
                print(line, end = '')

def main():
    files = sys.argv[1:]
    if(files):
        tac(files)
    else:
        print('usage: tac file1 [file2 ...]', file=sys.stderr)

if __name__ == '__main__':
    main()
