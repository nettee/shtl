#!/usr/bin/python3.2

import sys

argv = sys.argv[1:]

if argv:
    string = argv[0]
else:
    string = 'y'

while True:
    print(string)
