#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k54.py
from xml.etree import ElementTree as ET

if __name__ == '__main__':
    filename = "../data/nlp.txt.xml"
    root = ET.parse(filename)

    for token in root.iter('token'):
        word = token.findtext('word')
        lemma = token.findtext('lemma')
        pos = token.findtext('POS')
        print('\t'.join([word, lemma, pos]))
