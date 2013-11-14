import sys

def is_empty_line(line):
    return line == '\n'

def open_files(files):
    file_content = []
    if not files:
        file_content = [sys.stdin]
    for each_file in files:
        if each_file == '-':
            file_content.append(sys.stdin)
        else:
            fobj = open(each_file, 'r')
            file_content.append(fobj)

    return tuple(file_content)

def fopen_named(files):
    file_content = []
    if not files:
        file_content = [('', sys.stdin)]
    for each_file in files:
        if each_file == '-':
            file_content.append(('-', sys.stdin))
        else:
            fobj = open(each_file, 'r')
            file_content.append((each_file, fobj))

    return tuple(file_content)

def close_files(file_content):
    for fobj in file_content:
        if fobj != sys.stdin:
            fobj.close()


