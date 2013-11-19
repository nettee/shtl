import sys

def is_null_line(line):
    return line == '\n'

def fopen(files, mode='r'):
    file_content = []
    if not files:
        file_content = [sys.stdin]
    for each_file in files:
        if each_file == '-':
            file_content.append(sys.stdin)
        else:
            fobj = open(each_file, mode=mode)
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

def fclose(file_content):
    for fobj in file_content:
        if fobj != sys.stdin:
            fobj.close()

def fclose_named(file_content):
    for fname, fobj in file_content:
        if fobj != sys.stdin:
            fobj.close()


def billy(charset):
    """ translate the regular expression in charset to equivalent string
    """
    return charset
