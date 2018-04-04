#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k23.py

import re

from utils.json import extract_from_json

if __name__ == '__main__':
    lines = extract_from_json("イギリス").split('\n')

    for line in lines:
        section = re.search('^(=+)([^=]*)(=+)$', line)
        if section is not None:
            print("{0}:{1}".format(section.group(2), len(section.group(1)) - 1))
