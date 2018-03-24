#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k5.py
from utils.n_gram import N_Gram

if __name__ == '__main__':
    str = "I am an NLPer"
    n = N_Gram()

    print("単語bi-gram")
    print(n.bi_gram(str.split(" ")))

    print("文字bi-gram")
    print(n.bi_gram(list(str)))
