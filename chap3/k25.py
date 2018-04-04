#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k25.py

import re

from utils.json import extract_from_json

if __name__ == '__main__':
    lines = re.split("\n[\|}]", extract_from_json("イギリス"))
    information = {}

    row = re.compile("^(.+)\s=\s(.+)")
    for line in lines:
        r = row.search(line)
        if r:
            information[r.group(1).strip()] = r.group(2).strip()

    for k, v in information.items():
        print("({0} : {1})".format(k, v))
