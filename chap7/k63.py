#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k63.py
import json

from chap7.utils import open_gzip
import redis

if __name__ == '__main__':
    pool = redis.ConnectionPool(host='localhost', port=6379, db=1)
    db = redis.StrictRedis(connection_pool=pool)

    if not db.keys():
        for artist in open_gzip():
            if artist.get('tags', ''):
                db.set(artist['name'], json.dumps(artist['tags']))

    for tag in json.loads(db.get('Oasis').decode()):
        print("{}\t{}".format(tag['value'], tag['count']))
