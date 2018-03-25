#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k16.py
import os
import sys


def n_split(file_name, n):
    data = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        if len(lines) % n != 0:
            raise Exception("Undividable by N=%d" % n)
        else:
            num = len(lines) // n
            for i in range(n):
                start = num * i
                end = num * (i + 1) if i < n else n
                data.append(lines[start:end])
            return data


if __name__ == '__main__':
    file_name, n = sys.argv[1], int(sys.argv[2])
    data = n_split(file_name, n)
    dir = os.path.split(file_name)[0]
    for i, data in enumerate(n_split(file_name, n), start=1):
        path = os.path.join(dir, "file{}.txt".format(i))
        with open(path, 'w') as file:
            file.writelines(data)
