#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k18.py
import sys


def sort_by_item(file_name, n):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        lines = [line.split('\t') for line in lines]
        return sorted(lines, key=lambda x: float(x[n - 1]), reverse=True)


if __name__ == '__main__':
    file_name, n = sys.argv[1], int(sys.argv[2])

    for line in sort_by_item(file_name, n):
        print("\t".join(line), end='')
