#!/usr/bin/python3.2

# version: 0.7.8
# 2013-11-12
# 

"""
       join - join lines of two files on a common field
SYNOPSIS
       join [OPTION]... FILE1 FILE2
DESCRIPTION
       For  each pair of input lines with identical join fields, 
       write a line to standard output.  The default join field is the first, 
       delimited  by  whitespace. When FILE1 or FILE2 (not both) is -, 
       read standard input.
"""

import sys
import argparse

import stil

def join(file_content):
    tag_map = dict()
    for fobj in file_content:
        for line in fobj:
            line = line.strip()
            tag, line = line.split(' ', 1)
            if tag in tag_map:
                tag_map[tag].append(line)
            else:
                tag_map[tag] = [line]

    for tag in tag_map:
        print(tag, end='\t')
        print('\t'.join(tag_map[tag]))

def parse():
    parser = argparse.ArgumentParser(
            description='join lines of two files on a common field')
    parser.add_argument('files', nargs=2)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse()
    file_content = stil.fopen(args.files)
    join(file_content)
    stil.fclose(file_content)
