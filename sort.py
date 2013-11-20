#!/usr/bin/python3.2

# version: 0.0.1
# 2013-11-20

"""
    sort lines of text files
    slightly different from unix version
    aiming at simplicity
"""

import sys
import argparse

import stil

def shape(file_content, args):
    """ for each line in each file, process each line to
    the shape which user want
    return a generator
    """
    for fobj in file_content:
        for line in fobj:
            line = line.rstrip('\n')
            yield line

def sort(lines, args):
    return sorted(lines)


def parse():
    parser = argparse.ArgumentParser(
            description='sort lines of text files')
    parser.add_argument('files', nargs='*')

    return parser.parse_args()

if __name__ == '__main__':
    args = parse()
    file_content = stil.fopen(args.files)
    
    lines = sort(shape(file_content, args), args)
    for line in lines:
        print(line)

    stil.fclose(file_content)



