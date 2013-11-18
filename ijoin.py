#!/usr/bin/python3.2

"""ijoin.py
like join, but work in a single file
the input stream can either from stdin, 
    or from file(argument)
"""

import sys
import argparse

import stil

def ijoin(file_content):
    collect = dict()
    for fobj in file_content:
        for line in fobj:
            words = line.rstrip('\n').split()
            foreword = words[0]
            otherwords = '\t'.join(words[1:])
            if foreword in collect:
                collect[foreword].append(otherwords)
            else:
                collect[foreword] = [otherwords]
    
    for foreword in collect:
        print(foreword, end = '\t')
        print('\t'.join(collect[foreword]))

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse()
    file_content = stil.fopen(args.files)

    ijoin(file_content)

    stil.fclose(file_content)
