#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k57.py
from xml.etree import ElementTree as ET

from chap5.utils import graph_from_edges

if __name__ == '__main__':
    filename = "../data/nlp.txt.xml"
    root = ET.parse(filename)

    for sentence in root.iterfind('./document/sentences/sentence'):
        sentence_id = int(sentence.get('id'))
        edges = []

        for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):
            if dep.get('type') == 'punct':
                continue

            governor = dep.find('./governor')
            dependent = dep.find('.dependent')
            edges.append((
                (governor.get('idx'), governor.text),
                (dependent.get('idx'), dependent.text)
            ))

        if edges:
            graph = graph_from_edges(edges)
            graph.write_png('../data/57/{}.png'.format(sentence_id))
