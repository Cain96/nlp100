#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k42.py
from chap5.utils import dependencies

if __name__ == '__main__':
    for chunks in dependencies():
        for chunk in chunks:
            if chunk.has_depend and chunk.surface and chunks[chunk.dst].surface:
                print("\t".join([chunk.surface, chunks[chunk.dst].surface]))
