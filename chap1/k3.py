#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k3.py

if __name__ == '__main__':
    pi = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    words = pi.split(" ")
    words = [len(word.strip(",.")) for word in words]
    print(words)
