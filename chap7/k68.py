#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k68.py
from chap7.utils import mongo_connect
import pymongo

if __name__ == '__main__':
    collection = mongo_connect()

    top_artists = collection.find({'tags.value': 'dance'}).sort([('rating.count', pymongo.DESCENDING)])[:10]

    for i, artist in enumerate(top_artists, start=1):
        print("No.{}\t{}".format(i, artist['name']))
