#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k29.py

import re

import requests
from utils import extract_from_json

if __name__ == '__main__':
    lines = re.split("\n[\|}]", extract_from_json("イギリス"))
    information = {}

    row = re.compile("^(.+)\s=\s(.+)")
    markup = re.compile("'{2,5}")
    markup2 = re.compile(r"\[\[(.+?)\]\]")
    markup3 = re.compile(r"(.*\|)*(.*)")
    markup4 = re.compile(r"\{\{(.*\|)*(.*)\}\}")
    tag = re.compile(r"<.*>")
    link = re.compile(r"\[.*\]")

    for line in lines:
        r = row.search(line)
        if r:
            line = markup.sub("", r.group(2).strip())
            line = markup2.sub(lambda match: markup3.search(match.group(1)).group(2), line)
            line = markup4.sub(r"\2", line)
            line = tag.sub("", line)
            line = link.sub("", line)
            information[r.group(1).strip()] = line

    url = "https://en.wikipedia.org/w/api.php"
    payload = {"action": "query",
               "titles": "File:{}".format(information["国旗画像"]),
               "prop": "imageinfo",
               "format": "json",
               "iiprop": "url"}

    data = requests.get(url, payload).json()
    print(data['query']['pages'].popitem()[1]['imageinfo'][0]['url'])
