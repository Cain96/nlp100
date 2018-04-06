#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k31.py

from chap4.utils import morphological

if __name__ == '__main__':

    for sentence in morphological():
        for word in sentence:
            if word["pos"] == "動詞":
                print(word["surface"])
