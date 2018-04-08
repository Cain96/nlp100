#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k43.py
from chap5.utils import dependencies

if __name__ == '__main__':
    for chunks in dependencies():
        for chunk in chunks:
            if chunk.has_depend:
                dst_chunk = chunks[chunk.dst]
                if chunk.surface and dst_chunk.surface and chunk.has_pos("名詞") and dst_chunk.has_pos("動詞"):
                    print("\t".join([chunk.surface, dst_chunk.surface]))
