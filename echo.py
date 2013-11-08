#!/usr/bin/python3.2

import sys
import argparse

"""echo 
version 1.1.4
simulate shell program 'echo'
have argument -n -e -E
"""

def echo(args):
    if args.e and not args.E:
        args.string = eval('"""' + args.string.__str__() + '"""')

    if args.n:
        endline = ''
    else:
        endline = '\n'

    print(args.string, end=endline)

def parse():
    parser = argparse.ArgumentParser(
            description='display a line of text')
    parser.add_argument('string', 
            help='display the string to standard output')
    parser.add_argument('-n', action='store_true',
            help='do not output the trailing newline')
    parser.add_argument('-e', action='store_true',
            help='enable interpretation of backslash')
    parser.add_argument('-E', action='store_true',
            help='disable interpretaion of backslash (default)')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse()
    echo(args)
