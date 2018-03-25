#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k10.py
import sys


def count_lines(file_name):
    with open(file_name, 'r') as file:
        return len(file.readlines())


if __name__ == '__main__':
    file_name = sys.argv[1]
    print(count_lines(file_name))
