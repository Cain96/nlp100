#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


def extract_from_json(title):
    with open("../data/jawiki-country.json", 'r') as file:
        line = file.readline()
        while line:
            article_dict = json.loads(line)
            if article_dict["title"] == title:
                return article_dict["text"]
                break
            line = file.readline()
    return ""
