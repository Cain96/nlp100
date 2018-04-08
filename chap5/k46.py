#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k46.py
from chap5.utils import dependencies

if __name__ == '__main__':
    for chunks in dependencies():
        for chunk in chunks:
            verb = chunk.get_morphs_by_pos("動詞")
            if verb:
                verb = verb.base
                particles = []
                for src in chunk.srcs:
                    particles.extend(chunks[src].get_morphs_surfaces_by_pos("助詞"))
                if particles:
                    particles = sorted(particles, key=lambda particle: (particle[0], particle[1]))
                    particles = list(zip(*particles))
                    print("\t".join([verb, " ".join(particles[0]), " ".join(particles[1])]))
