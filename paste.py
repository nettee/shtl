#!/usr/bin/python3.2

# version: 1.2.3
# 2013-11-12
# support arbitary input files

"""
       paste - merge lines of files
SYNOPSIS
       paste [OPTION]... [FILE]...
DESCRIPTION
       Write  lines  consisting  of the sequentially corresponding lines from each FILE, sepa‐
       rated by TABs, to standard output.  With no FILE, or when  FILE  is  -,  read  standard
       input.
"""


import sys
from itertools import zip_longest
import argparse

def display(file_content, delimiters=None, parallel=True):
    if parallel:
        for things in zip_longest(*file_content, fillvalue=''):
            things = (string.rstrip('\n') for string in things)
            if delimiters is None:
                print('\t'.join(things))
            else:
                print('unsupported feature', file=sys.stderr)
    else:
        for fobj in file_content:
            lines = (line.rstrip('\n') for line in fobj)
            print('\t'.join(lines))

def paste(args):
    files = args.files
    file_content = []

    if not files:
        file_content = [sys.stdin]
    else:
        for each_file in files:
            if each_file == '-':
                file_content.append(sys.stdin)
            else:
                fobj = open(each_file, 'r')
                file_content.append(fobj)

    display(file_content, args.delimiters, parallel=(not args.serial))
    for each_fobj in file_content:
        if each_fobj != sys.stdin:
            each_fobj.close()

def parse():
    parser = argparse.ArgumentParser(
            description='merge lines of files')
    parser.add_argument('files', nargs='*')
    parser.add_argument('-d', '--delimiters',
            help='reuse characters from LIST instead of TABs')
    parser.add_argument('-s', '--serial', action='store_true',
            help='paste one file at a time instead of in parallel')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse()
    paste(args)
    
