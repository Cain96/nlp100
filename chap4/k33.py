#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k33.py

from chap4.utils import morphological

if __name__ == '__main__':

    for sentence in morphological():
        for word in sentence:
            if word["pos"] == "名詞" and word["pos1"] == "サ変接続":
                print(word["surface"])
