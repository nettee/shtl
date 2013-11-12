#!/usr/bin/python3.2

import sys

argv = sys.argv[1:]

if argv:
    s = argv[0]
else:
    s = 'y'

while True:
    print(s)
