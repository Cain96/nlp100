#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k62.py
import redis

if __name__ == '__main__':
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    db = redis.StrictRedis(connection_pool=pool)
    japanese_artists = [artist for artist in db.keys() if db.get(artist.decode()).decode() == 'Japan']
    print(len(japanese_artists))
