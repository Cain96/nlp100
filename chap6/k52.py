#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k52.py
from chap6.utils import get_words, stemming

if __name__ == '__main__':
    words = [word.lower() for word in get_words()]
    for word in stemming(words):
        print(word[0], word[1], sep='\t')
