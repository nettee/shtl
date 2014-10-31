#!/usr/bin/python3.2

import sys
import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('strings', nargs='*')
    
    return parser.parse_args()

if __name__ == '__main__':
    args = parse()
    if args.strings:
        strings = ' '.join(args.strings)
    else:
        strings = 'y'
    try:
        while True:
            print(strings)
    except KeyboardInterrupt:
        sys.exit(0)
