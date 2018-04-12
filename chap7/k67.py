#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k67.py
from chap7.utils import mongo_connect

if __name__ == '__main__':
    collection = mongo_connect()

    oasis = list(collection.find({'aliases.name': 'オアシス'}))
    for data in oasis:
        print(oasis)
