#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k44.py
from chap5.utils import dependencies, graph_from_edges

if __name__ == '__main__':
    N = 4
    for i, chunks in enumerate(dependencies()):
        edges = []
        if i == N:
            for j, chunk in enumerate(chunks):
                if chunk.has_depend:
                    dst_chunk = chunks[chunk.dst]
                    if chunk.surface and dst_chunk.surface:
                        edges.append(((j, chunk.surface), (chunk.dst, dst_chunk.surface)))
            break

    if len(edges) > 0:
        graph = graph_from_edges(edges)
        graph.write_png('../data/result.png')
