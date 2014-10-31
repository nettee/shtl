#!/usr/bin/python3.2

# version: 2.2.0
# 2013-11-12
# support -n -E -T -s -b arguments
# support '-' from standard input

"""
       cat - concatenate files and print on the standard output
SYNOPSIS
       cat [OPTION]... [FILE]...
"""


import sys
import argparse

import stil

line_count = 1

def cat(fileobj, args):
    global line_count
    last_line = None
    for line in fileobj:
        if args.show_tabs:
            line = line.replace('\t', '^I')

        if args.squeeze_blank:
            if stil.is_null_line(line) and stil.is_null_line(last_line):
                continue  # ignore current line

        if args.number_nonblank:
            if not stil.is_null_line(line):
                print('{0:>6}  '.format(line_count), end='')
                line_count += 1
        elif args.number:
            print('{0:>6}  '.format(line_count), end='')
            line_count += 1

        if args.show_ends:
            line = line[:-1] + '$\n'

        print(line, end='')
        last_line = line

def parse():
    parser = argparse.ArgumentParser(
            description='concatenate files and print on the standard output')
    parser.add_argument('files', nargs='*')
    parser.add_argument('-n', '--number', action='store_true',
            help='number all output lines')
    parser.add_argument('-E', '--show-ends', action='store_true',
            help='display $ at end of each line')
    parser.add_argument('-T', '--show-tabs', action='store_true',
            help='display TAB characters as ^I')
    parser.add_argument('-b', '--number-nonblank', action='store_true',
            help='number nonempty output lines, overrides -n')
    parser.add_argument('-s', '--squeeze-blank', action='store_true',
            help='suppress repeated empty output lines')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse()

    file_content = stil.fopen(args.files)
    for fobj in file_content:
        cat(fobj, args)

    stil.fclose(file_content)
