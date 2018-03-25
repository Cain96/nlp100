#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k13.py
import os
import sys


def get_col(file_names):
    data = []
    for file_name in file_names:
        with open(file_name, 'r') as file:
            data.append([line.strip() for line in file.readlines()])
    return zip(*data)


if __name__ == '__main__':
    file_names = sys.argv[1:]
    dir = os.path.split(file_names[0])[0]
    path = os.path.join(dir, "merge.txt")
    lines = get_col(file_names)
    with open(path, 'w') as file:
        lines = ['\t'.join(line) for line in lines]
        lines = [line + '\n' for line in lines]
        file.writelines(lines)
