#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k58.py
from xml.etree import ElementTree as ET

from chap5.utils import Dependant

if __name__ == '__main__':
    filename = "../data/nlp.txt.xml"
    root = ET.parse(filename)

    for sentence in root.iterfind('./document/sentences/sentence'):
        dependent_dict = {}
        sentence_id = int(sentence.get('id'))

        for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):
            type = dep.get('type')
            if type == 'nsubj' or type == 'dobj':
                governor = dep.find('./governor')
                idx = governor.get('idx')
                if idx not in dependent_dict:
                    dependent_dict[idx] = Dependant(governor.text)

                dependent = dep.findtext('./dependent')
                if type == 'nsubj':
                    dependent_dict[idx].set_subject(dependent)
                else:
                    dependent_dict[idx].set_object(dependent)

        dependent_list = [dependent for dependent in dependent_dict.items() if dependent[1].has_all_attribute()]
        for dependent in map(lambda x: x[1], sorted(dependent_list, key=lambda x: x[0])):
            print("\t".join([dependent.subject, dependent.predicate, dependent.object]))
