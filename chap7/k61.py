#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k61.py
import redis

if __name__ == '__main__':
    db = redis.StrictRedis(host='localhost', port=6379, db=0)

    print(db.get("エレファントカシマシ").decode())
