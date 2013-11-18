#!/usr/bin/python3.2

# version 2.1.3
# 2013-11-18

"""
   cut - remove sections from each line of files
   cut OPTION... [FILE]...
   Print selected parts of lines from each FILE to standard output.
"""

import sys
import argparse

import stil

def extract(fields, script):
    if not script:
        return fields

    sfields = []

    if ',' in script:
        scripts = script.split(',')
    else:
        scripts = [script]

    for each_script in scripts:
        if '-' in each_script:
            a, b = map(int, each_script.split('-'))
            for j in range(a, b+1):
                sfields.append(fields[j-1])
        else:
            sfields.append(fields[int(each_script)-1])

    return sfields

def cut(fobj, args):
    for line in fobj:
        line = line.rstrip('\n')
        fields = line.split(args.delimiter)
        sfields = extract(fields, args.fields)
        print(args.output_delimiter.join(sfields))

def parse():
    parser = argparse.ArgumentParser(
            description='remove sections from each line of files')
    parser.add_argument('files', nargs='*')
    parser.add_argument('-d', '--delimiter', default='\t',
            help='use DELIM instead of TAB for field delimiter')
    parser.add_argument('-f', '--fields',
            help='select only these fields')
    parser.add_argument('--output-delimiter', help='use  STRING  as  the  output delimiter the default is to use the input delimiter')

    return parser.parse_args()

if __name__ == '__main__':
    args = parse()
    if not args.output_delimiter:
        args.output_delimiter = args.delimiter

    file_content = stil.fopen(args.files)
    for fobj in file_content:
        cut(fobj, args)
    stil.fclose(file_content)
