#!/usr/bin/python3.2

# version: 1.6.3
# 2013-11-11
# support arbitary number of arguments
# support -l, -w, -m, -L arguments


import sys
import argparse

def count_file(fobj):

    line_count = 0
    word_count = 0
    character_count = 0
    max_len = 0

    for line in fobj:
        line_count += 1
        character_count += len(line)
        word_count += len(line.split())

        length = len(line)
        if length > max_len:
            max_len = length

    return (line_count, word_count, character_count, max_len)

def fmt_str(args):
    fmt_strings = []
    if args.max_len:
        return "{0[3]:>3}"

    if args.lines:
        fmt_strings.append("{0[0]:>3}")
    if args.words:
        fmt_strings.append("{0[1]:>3}")
    if args.chars:
        fmt_strings.append("{0[2]:>3}")
    if fmt_strings:
        return ' '.join(fmt_strings)
    else:
        return "{0[0]:>3} {0[1]:>3} {0[2]:>3}"

def display(fmt_string, the_result, filename):
    if filename is None:
        print(fmt_string.format(the_result))
    else:
        print(fmt_string.format(the_result), end=' ')
        print(filename)

def wc(args):
    files = args.files
    fmt_string = fmt_str(args)

    if not files:   # from standard input
        result = count_file(sys.stdin)
        display(fmt_string, result, filename=None)

    elif len(files) == 1:    # single origin file
        with open(files[0], 'r') as fobj:
            result = count_file(fobj)
            display(fmt_string, result, files[0])

    else:   # multiple origin file
        total_result = [0, 0, 0, 0]
        for each_file in files:
            with open(each_file, 'r') as fobj:
                result = count_file(fobj)
                display(fmt_string, result, each_file)
                for i in (0, 1, 2):
                    total_result[i] += result[i]
                if result[3] > total_result[3]:
                    total_result[3] = result[3]

        display(fmt_string, total_result, 'total')
                



def parse():
    parser = argparse.ArgumentParser(
            description='print newline, words and charactor counts for each file')
    parser.add_argument('files', nargs='*')
    parser.add_argument('-l', '--lines', action='store_true',
                help='print the newline counts') 
    parser.add_argument('-w', '--words', action='store_true',
                help='print the word counts')   
    parser.add_argument('-m', '--chars', action='store_true',
                help='print the character counts')
    parser.add_argument('-L', '--max-line-length', action='store_true',
                dest='max_len', help='print the character counts')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse()
    wc(args)
    
