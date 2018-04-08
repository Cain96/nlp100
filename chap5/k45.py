#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k45.py
from chap5.utils import dependencies

if __name__ == '__main__':
    output = []
    for chunks in dependencies():
        for chunk in chunks:
            verb = chunk.get_morphs_by_pos("動詞")
            if verb:
                verb = verb[0].base
                particles = [chunks[src].get_morphs_by_pos("助詞") for src in chunk.srcs]
                if particles:
                    particles = sorted(map(lambda particle: particle.base, particles))
                    output.append("\t".join([verb, " ".join(particles)]) + "\n")

    with open("../data/45.txt", "w") as file:
        file.writelines(output)
