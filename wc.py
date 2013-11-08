#!/usr/bin/python3.2

import argparse
import sys

def count_file(fobj):
    line_count = 0
    word_count = 0
    character_count = 0
    for line in fobj:
        line_count += 1
        character_count += len(line)
        word_count += len(line.split())
    return (line_count,
            word_count,
            character_count)


def wc(args):
    files = args.files
    if not files:
        result = count_file(sys.stdin)
    elif len(files) == 1:
        with open(files[0], 'r') as fobj:
            result = count_file(fobj)
            print('{0[0]:>3} {0[1]:>3} {0[2]:>3} {1}'.format(result, files[0]))
    else:
        for each_file in files:
            with open(each_file, 'r') as fobj:
                result = count_file(fobj)
                print('{0[0]:>3} {0[1]:>3} {0[2]:>3} {1}'.format(
                                                            result, each_file))


def parse():
    parser = argparse.ArgumentParser(
            description='print newline, words and charactor counts for each file')
    parser.add_argument('files', nargs='*')
    parser.add_argument('-l')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse()
    wc(args)
    
