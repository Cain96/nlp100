#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k53.py
from xml.etree import ElementTree as ET

if __name__ == '__main__':
    filename = "../data/nlp.txt.xml"
    root = ET.parse(filename)

    for word in root.iter('word'):
        print(word.text)
