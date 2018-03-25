#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k15.py

import sys


def tail(file_name, n):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return "".join(lines[-min(n, len(lines)):])


if __name__ == '__main__':
    file_name, n = sys.argv[1], int(sys.argv[2])
    print(tail(file_name, n), end='')
