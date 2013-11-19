#!/usr/bin/python3.2

# version:1.3.1
# 2013-11-19

"""
   tr - translate or delete characters
   tr [OPTION]... SET1 [SET2]
   Translate, squeeze, and/or delete characters from standard input, 
   writing to standard output.
"""

import sys
import argparse

import stil

def re2str(charset, state='in'):
    """ translate the regular expression in charset to equivalent string
        ## not accomplished yet
    """
    return charset

def delete(args):
    charset = re2str(args.set1, state='in')

    for line in sys.stdin:
        line = line.rstrip('\n')
        print(''.join(c for c in line if c not in charset))

def translate(args):
    charset_in = re2str(args.set1, state='in')
    charset_out = re2str(args.set2, state='out')
    char_trans = dict(zip(charset_in, charset_out))
    
    for line in sys.stdin:
        line = line.rstrip('\n')
        print(''.join(char_trans[c] if c in char_trans else c for c in line))

def parse():
    parser = argparse.ArgumentParser(
            description='translate or delete characters')
    parser.add_argument('set1')
    parser.add_argument('set2', nargs='?', default=None)
    parser.add_argument('-d', '--delete', action='store_true',
            help='delete characters in SET1, do not translate')

    return parser.parse_args()

if __name__ == '__main__':
    args = parse()
    if args.set2 is None:
        if args.delete:
            delete(args)
        else:
            print('tr: operand miss after "{}"'.format(args.set1), 
                "try tr --help for more information.", 
                sep='\n', file=sys.stderr)
            sys.exit(1)
    else:
        translate(args)

