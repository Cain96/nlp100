#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k35.py
from chap4.utils import morphological

if __name__ == '__main__':
    long_nouns = []

    for sentence in morphological():
        nouns = []
        for word in sentence:
            if word["pos"] == "名詞":
                nouns.append(word["surface"])
            else:
                if len(nouns) > 1:
                    long_nouns.append("".join(nouns))
                nouns = []

        if len(nouns) > 1:
            long_nouns.append("".join(nouns))

    print(long_nouns)
