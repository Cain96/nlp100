#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k17.py
import sys


def sort_str(file_name, n):
    data = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.split('\t')
            data.append(line[n - 1])
        return sorted(list(set(data)))


if __name__ == '__main__':
    file_name, n = sys.argv[1], int(sys.argv[2])
    for x in sort_str(file_name, n):
        print(x)
