#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k27.py

import re

from utils import extract_from_json

if __name__ == '__main__':
    lines = re.split("\n[\|}]", extract_from_json("イギリス"))
    information = {}

    row = re.compile("^(.+)\s=\s(.+)")
    markup = re.compile("'{2,5}")
    markup2 = re.compile(r"\[\[(.+?)\]\]")
    markup3 = re.compile(r"(.*\|)*(.*)")

    for line in lines:
        r = row.search(line)
        if r:
            line = markup.sub("", r.group(2).strip())
            line = markup2.sub(lambda match: markup3.search(match.group(1)).group(2), line)
            information[r.group(1).strip()] = line

    for k, v in information.items():
        print("({0} : {1})".format(k, v))
