#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k21.py
import re

from utils.json import extract_from_json

if __name__ == '__main__':
    lines = extract_from_json("イギリス").split('\n')

    for line in lines:
        category = re.search('^\[\[Category:(.+)(\|.+)?\]\]$', line)
        if category is not None:
            print(category.group())
