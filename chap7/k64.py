#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k64.py
from chap7.utils import open_gzip
import pymongo
from pymongo import MongoClient

if __name__ == '__main__':
    unit_bulk = 10000

    clinet = MongoClient('localhost', 27017)
    db = clinet.testdb
    collection = db.artist

    buf = []
    for i, artist in enumerate(open_gzip(), start=1):
        buf.append(artist)

        if i % unit_bulk == 0:
            collection.insert_many(buf)
            buf = []
            print("{}件追加完了".format(i))

    if len(buf) > 0:
        collection.insert_many(buf)
        print("{}件追加完了".format(i))

    collection.create_index([('name', pymongo.ASCENDING)])
    collection.create_index([('aliases.name', pymongo.ASCENDING)])
    collection.create_index([('tags.value', pymongo.ASCENDING)])
    collection.create_index([('rating.value', pymongo.ASCENDING)])
