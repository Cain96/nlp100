#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k48.py
from chap5.utils import dependencies

if __name__ == '__main__':
    output = []
    for chunks in dependencies():
        for chunk in chunks:
            if chunk.has_pos("名詞"):
                path = chunk.path_to_root(chunks)
                if path:
                    print(" -> ".join(map(lambda chunk: chunk.surface, path)))
