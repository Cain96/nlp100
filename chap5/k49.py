#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k49.py
import itertools

from chap5.utils import dependencies

if __name__ == '__main__':
    for chunks in dependencies():
        noun_pairs = list(itertools.combinations([chunk for chunk in chunks if chunk.has_pos("名詞")], 2))

        for i, j in noun_pairs:
            noun_i, noun_j = i.get_morphs_by_pos("名詞"), j.get_morphs_by_pos("名詞")
            surface_i, surface_j = noun_i.surface, noun_j.surface
            noun_i.surface, noun_j.surface = "X", "Y"
            path_i, path_j = i.path_to_root(chunks), j.path_to_root(chunks)

            if j in path_i:
                print(" -> ".join(map(lambda chunk: chunk.surface, path_i[0:path_i.index(j) + 1])))
            else:
                union = sorted(set(path_i) & set(path_j), key=path_i.index)
                if union:
                    k = union[0]
                    output = [
                        " -> ".join(map(lambda chunk: chunk.surface, path_i[0:path_i.index(k)])),
                        " -> ".join(map(lambda chunk: chunk.surface, path_j[0:path_j.index(k)])),
                        k.surface
                    ]
                    print(" | ".join(output))
            noun_i.surface, noun_j.surface = surface_i, surface_j
