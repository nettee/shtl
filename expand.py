#!/usr/bin/python3.2

# version: 1.1.0
# 2013-11-14
# 

"""
       expand - convert tabs to spaces
SYNOPSIS
       expand [OPTION]... [FILE]...
DESCRIPTION
       Convert  tabs in each FILE to spaces, writing to standard output.  With
       no FILE, or when FILE is -, read standard input.

       Mandatory arguments to long options are  mandatory  for  short  options
       too.
"""

import sys
import argparse

import stil

def expand(fobj, args):
    tabsize = args.tabs
    for line in fobj:
        print(line.expandtabs(tabsize), end='')

def parse():
    parser = argparse.ArgumentParser(
            description='convert tabs to spaces')
    parser.add_argument('files', nargs='*')
    parser.add_argument('-t', '--tabs', default=8,
            help='have tabs NUMBER characters apart, not 8')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse()

    file_content = stil.fopen(args.files)
    for fobj in file_content:
        expand(fobj, args)
    stil.fclose(file_content)
