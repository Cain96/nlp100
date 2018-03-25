#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k19.py

from collections import Counter
import sys


def sort_by_frequency(file_name, n):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        words = [line.split('\t')[n - 1] for line in lines]
        counter = Counter(words)
        return [word for word, value in counter.most_common()]


if __name__ == '__main__':
    file_name, n = sys.argv[1], int(sys.argv[2])

    for word in sort_by_frequency(file_name, n):
        print(word)
