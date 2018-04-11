#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k55.py
from xml.etree import ElementTree as ET

if __name__ == '__main__':
    filename = "../data/nlp.txt.xml"
    root = ET.parse(filename)

    for token in root.iterfind(
            './document/sentences/sentence/tokens/token[NER="PERSON"]'
    ):
        print(token.findtext('word'))
