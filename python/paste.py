#!/usr/bin/python3.2

# version: 1.5.0
# 2013-11-18
# support arbitary input files
# support -s argument

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

import stil

def paste(file_content, args):
    if not args.serial:
        for things in zip_longest(*file_content, fillvalue=''):
            things = (string.rstrip('\n') for string in things)
            print('\t'.join(things))
    else:
        for fobj in file_content:
            lines = (line.rstrip('\n') for line in fobj)
            print('\t'.join(lines))

def parse():
    parser = argparse.ArgumentParser(
            description='merge lines of files')
    parser.add_argument('files', nargs='*')
    #parser.add_argument('-d', '--delimiters',
    #        help='reuse characters from LIST instead of TABs')
    parser.add_argument('-s', '--serial', action='store_true',
            help='paste one file at a time instead of in parallel')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse()
    file_content = stil.fopen(args.files)

    paste(file_content, args)

    stil.fclose(file_content)
    
