#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k60.py
from chap7.utils import open_gzip
import redis

if __name__ == '__main__':
    db = redis.StrictRedis(host='localhost', port=6379, db=0)

    if not db.keys():
        for artist in open_gzip():
            db.set(artist['name'], artist.get('area', ''))
