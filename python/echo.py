#!/usr/bin/python3.2

# version: 1.2.4
# 2013-11-12
# support -n -e -E argument

"""
       echo - display a line of text
SYNOPSIS
       echo [OPTION]... [STRING]...
"""

import sys
import argparse

def echo(args):
    if args.e and args.E:  # note E stores False
        # call eval to automatically escape backslash
        string = eval('"""' + args.string.__str__() + '"""')
    else:
        string = args.string

    if args.n:
        eol = ''
    else:
        eol = '\n'

    print(string, end=eol)

def parse():
    parser = argparse.ArgumentParser(
            description='display a line of text')
    parser.add_argument('string', 
            help='display the string to standard output')
    parser.add_argument('-n', action='store_true',
            help='do not output the trailing newline')
    parser.add_argument('-e', action='store_true',
            help='enable interpretation of backslash')
    parser.add_argument('-E', action='store_false',
            help='disable interpretaion of backslash (default)')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse()
    echo(args)
