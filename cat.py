#!/usr/bin/python3.2

# version: 1.8.5
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

line_count = 1

def is_empty_line(line):
    return line == '\n'


def print_file(fileobj, args):
    global line_count
    last_line = None
    for line in fileobj:
        if args.show_tabs:
            line = line.replace('\t', '^I')

        if args.squeeze_blank:
            if is_empty_line(line) and is_empty_line(last_line):
                continue  # ignore current line

        if args.number_nonblank:
            if not is_empty_line(line):
                print('{0:>6}  '.format(line_count), end='')
                line_count += 1
        elif args.number:
            print('{0:>6}  '.format(line_count), end='')
            line_count += 1

        if args.show_ends:
            line = line[:-1] + '$\n'

        print(line, end='')
        last_line = line


def cat(args):
    line_count = 1  # initialization
    if args.files:
        for each_file in args.files:
            if each_file == '-':
                print_file(sys.stdin, args)
            else:
                with open(each_file, 'r') as fobj:
                    print_file(fobj, args)
    else:
        print_file(sys.stdin, args)


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
    cat(args)
