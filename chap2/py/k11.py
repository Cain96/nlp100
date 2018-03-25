#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k11.py
import sys


def tab_to_space(file_name):
    with open(file_name, 'r') as file:
        return ''.join([line.replace('\t', ' ') for line in file])


if __name__ == '__main__':
    file_name = sys.argv[1]
    print(tab_to_space(file_name), end='')
