#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k65.py
from chap7.utils import mongo_connect

if __name__ == '__main__':
    collection = mongo_connect()
    for data in collection.find({'name': 'Queen'}):
        print(data)
