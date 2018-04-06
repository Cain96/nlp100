#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k36.py

from collections import Counter

from chap4.utils import morphological

if __name__ == '__main__':
    counter = Counter()

    for sentence in morphological():
        counter.update([word['surface'] for word in sentence])

    for word, count in sorted(counter.most_common(), key=lambda x: (-x[1], x[0])):
        print(word, count)
