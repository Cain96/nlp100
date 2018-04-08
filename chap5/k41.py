#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k41.py
from chap5.utils import dependencies

if __name__ == '__main__':
    for i, sentence in enumerate(dependencies()):
        if i == 7:
            for chunk in sentence:
                print(chunk.surface)
            break
