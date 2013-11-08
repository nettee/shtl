#!/usr/bin/python3.2

"""expand.py
expand every tab at the beginnig of each line
into blanks, by default 4 blanks
"""

import sys

def expand(line, tabsize):
    return line.expandtabs(tabsize)

def main():
    if len(sys.argv) == 1:
        tabsize = 4
    else:
        tabsize = int(sys.argv[1])

    for line in sys.stdin:
        print(expand(line, tabsize), end = '')

if __name__ == '__main__':
    main()
