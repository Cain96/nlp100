#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k47.py
from chap5.utils import dependencies

if __name__ == '__main__':
    output = []
    for chunks in dependencies():
        for chunk in chunks:
            if chunk.has_sahen_wo and chunk.has_depend:
                dst = chunks[chunk.dst]
                verb = dst.get_morphs_by_pos("動詞")
                if verb:
                    verb = chunk.get_sahen_wo() + verb.base
                    src_chunks = [chunks[src] for src in dst.srcs if chunks[src] != chunk]
                    src_particles = [src_chunk.get_morphs_by_pos("助詞") for src_chunk in src_chunks
                                     if src_chunk.get_morphs_by_pos("助詞")]
                    src_pairs = [(particle.base, src_chunk.surface) for particle, src_chunk in
                                 zip(src_particles, src_chunks)]
                    if src_pairs:
                        src_pairs = sorted(src_pairs, key=lambda pair: (pair[0], pair[1]))
                        src_pairs = list(zip(*src_pairs))
                        output.append("\t".join([verb, " ".join(src_pairs[0]), " ".join(src_pairs[1])]) + "\n")

    with open("../data/47.txt", "w") as file:
        file.writelines(output)
