#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k30.py

from chap4.utils import morphological

if __name__ == '__main__':

    for sentence in morphological():
        for word in sentence:
            print(word["surface"], word["base"], word["pos"], word["pos1"])
