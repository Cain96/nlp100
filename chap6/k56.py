#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k56.py
from xml.etree import ElementTree as ET

if __name__ == '__main__':
    filename = "../data/nlp.txt.xml"
    root = ET.parse(filename)

    rep_dict = {}
    for coreference in root.iterfind('./document/coreference/coreference'):
        representative = coreference.findtext('./mention[@representative="true"]/text')

        for mention in coreference.iterfind('./mention'):
            if mention.get('representative', 'false') == 'false':
                sentence_id = int(mention.findtext('sentence'))
                start = int(mention.findtext('start'))
                end = int(mention.findtext('end'))

                if not (sentence_id, start) in rep_dict:
                    rep_dict[(sentence_id, start)] = (end, representative)

    for sentence in root.iterfind('./document/sentences/sentence'):
        sentence_id = int(sentence.get('id'))
        representative = ""
        rest = 0
        words = []

        for token in sentence.iterfind('./tokens/token'):
            token_id = int(token.get('id'))

            if rest == 0 and (sentence_id, token_id) in rep_dict:
                (end, representative) = rep_dict[(sentence_id, token_id)]
                rest = end - token_id

            words.append(token.findtext('word'))

            if rest == 0:
                print(words[0], end=" ")
                words = []

            if rest > 0:
                rest -= 1
                if rest == 0:
                    print("[{}] ({}) ".format(representative, " ".join(words)), end="")
                    words = []

        print()
