#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k2.py

if __name__ == '__main__':
    str1 = "パトカー"
    str2 = "タクシー"

    output = "".join(i + j for i, j in zip(str1, str2))

    print(output)
