#!/usr/bin/python3.2

# version: 2.5.0
# 2013-11-14
# support arbitary number of arguments
# support -l, -w, -m, -L arguments
# support '-' from standard input

"""
       wc - print newline, word, and characters for each file
       (note that this is slightly different from the real wc)
SYNOPSIS
       wc [OPTION]... [FILE]...
DESCRIPTION
       Print  newline,  word, and characters for each FILE, and a total line if more than one
       FILE is specified.  With no FILE, or when FILE is -, read standard input.  A word is  a
       non-zero-length sequence of characters delimited by white space.  The options may
       be used to select which counts are printed, always in  the  following  order:  newline,
       word, character, byte, maximum line length.

"""

import sys
import argparse

import stil

def count_file(fobj):

    line_count = 0
    word_count = 0
    char_count = 0
    max_len = 0

    for line in fobj:
        line_count += 1
        char_count += len(line)
        word_count += len(line.split())

        length = len(line)
        if length > max_len:
            max_len = length

    return (line_count, word_count, char_count, max_len)

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

def merge_result(results):
    (line_vec, word_vec, char_vec, max_len_vec) = zip(*results)
    return (sum(line_vec), sum(word_vec),
            sum(char_vec), max(max_len_vec))


def display(fmt_string, the_result, fname):
    print(fmt_string.format(the_result), fname)

def wc(args):
    file_content = stil.fopen_named(args.files)
    fmt_string = fmt_str(args)

    results = []

    for fname, fobj in file_content:
        result = count_file(fobj)
        results.append(result)
        print(fmt_string.format(result), fname)
    
    if len(file_content) > 1:
        total_result = merge_result(results)
        print(fmt_string.format(total_result), 'total')

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
