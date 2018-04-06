#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k34.py

from chap4.utils import morphological, n_gram

if __name__ == '__main__':

    for sentence in morphological():
        for first, second, third in n_gram(sentence, 3):
            if second["surface"] == "の" and first["pos"] == "名詞" and third["pos"] == "名詞":
                print(first["surface"] + second["surface"] + third["surface"])
