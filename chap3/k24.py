#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k24.py

import re

from utils.json import extract_from_json

if __name__ == '__main__':
    lines = extract_from_json("イギリス").split('\n')

    for line in lines:
        picture = re.search('(ファイル|File):(.+\.[a-z]+)\|', line)
        if picture is not None:
            print(picture.group(2))
