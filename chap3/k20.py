#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k20.py
import json

if __name__ == '__main__':
    with open("../data/jawiki-country.json", 'r') as file:
        line = file.readline()
        while line:
            article_dict = json.loads(line)
            if article_dict["title"] == "イギリス":
                print(article_dict["text"])
                break
            line = file.readline()
