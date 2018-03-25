#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k12.py
import os
import sys


def divide_col(file_name: str, num: int):
    with open(file_name, 'r') as file:
        return [line.split()[num - 1] + '\n' for line in file.readlines()]


if __name__ == '__main__':
    file_name, num = sys.argv[1], int(sys.argv[2])
    cols = divide_col(file_name, num)
    dir = os.path.split(file_name)[0]
    path = os.path.join(dir, "col{}.txt".format(num))
    with open(path, 'w') as file:
        file.writelines(cols)
