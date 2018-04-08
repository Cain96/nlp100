#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k40.py
from chap5.utils import dependencies

if __name__ == '__main__':
    for i, sentence in enumerate(dependencies()):
        if i == 2:
            for chunk in sentence:
                for morph in chunk.morphs:
                    print(morph)
            break
