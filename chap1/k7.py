#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k7.py

if __name__ == '__main__':
    def get_string(x, y, z):
        return "{x}時の{y}は{z}".format(x=x, y=y, z=z)

print(get_string(x=12, y="気温", z=22.4))
