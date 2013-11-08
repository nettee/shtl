#!/usr/bin/python3.2

"""ijoin.py
like join, but work in a single file
the input stream can either from stdin, 
    or from file(argument)
"""

import sys
import argparse

def ijoin(fobj):
    collect = dict()
    for line in fobj:
        words = line.split()
        foreword = words[0]
        otherwords = '\t'.join(words[1:])
        if foreword in collect:
            collect[foreword].append(otherwords)
        else:
            collect[foreword] = [otherwords]
    
    for foreword in collect:
        print(foreword, end = '\t')
        print('\t'.join(collect[foreword]))

if __name__ == '__main__':
    if sys.argv[1:]:
        filename = sys.argv[1]
        try:
            with open(filename, 'r') as fobj:
                ijoin(fobj)
        except IOError as err:
            print('error', str(err))
    else:
        ijoin(sys.stdin)
