# version: 0.6.0
# 2013-11-21

import sys

def is_null_line(line):
    return line == '\n'

def strethed(ls):
    result = []
    for item in ls:
        if isinstance(item, list):
            result.extend(strethed(item))
        else:
            result.append(item)

    return result

def putlist(ls, sep='\n'):
    print(sep.join(map(str, strethed(ls))))

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

def fclose(file_content):
    for fobj in file_content:
        if fobj != sys.stdin:
            fobj.close()

def billy(charset):
    """ translate the regular expression in charset to equivalent string
    """
    return charset

if __name__ == '__main__':
    putlist([1,[3,3,3,],5,6,7,[8,[9,[10,'a']]],111], sep=' ')
