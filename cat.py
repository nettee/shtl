#!/usr/bin/python3.2

import sys
import argparse

line_count = 1


def print_file(fileobj, args=None):
    global line_count
    for line in fileobj:
        if args.number:
            print('{0:>6}  '.format(line_count), end='')
            line_count += 1
        if args.show_ends:
            print(line[:-1], end='$\n')
        else:
            print(line, end='')


def cat(args):
    line_count = 1  # initialization
    if args.files:
        for each_file in args.files:
            with open(each_file, 'r') as fobj:
                print_file(fobj, args)
    else:
        print_file(sys.stdin)


def parse():
    parser = argparse.ArgumentParser(
            description='concatenate files and print on the standard output')
    parser.add_argument('files', nargs='*')
    parser.add_argument('-n', '--number', action='store_true',
            help='number all output lines')
    parser.add_argument('-E', '--show-ends', action='store_true',
            help='display $ at end of each line')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse()
    cat(args)
