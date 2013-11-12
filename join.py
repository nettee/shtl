#!/usr/bin/python3.2

# version: 0.5.6
# 2013-11-12
# 

"""
       join - join lines of two files on a common field
SYNOPSIS
       join [OPTION]... FILE1 FILE2
DESCRIPTION
       For  each pair of input lines with identical join fields, write a line to standard out‐
       put.  The default join field is the first, delimited  by  whitespace.   When  FILE1  or
       FILE2 (not both) is -, read standard input.
"""

import sys
import argparse

def join(file_content):
    pass

def join_files(args):
    files = args.files
    file_content = []
    for each_file in files:
        if each_file == '-':
            file_content.append(sys.stdin)
        else:
            fobj = open(each_file, 'r')
            file_content.append(fobj)

    join(file_content)

    for fobj in file_content:
        if fobj != sys.stdin:
            fobj.close()

def parse():
    parser = argparse.ArgumentParser(
            description='join lines of two files on a common field')
    parser.add_argument('files', nargs=2)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse()
    join_files(args)

