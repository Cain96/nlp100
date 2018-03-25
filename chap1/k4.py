#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k4.py


def get_element(index, word):
    if index in one_letters:
        return word[:1]
    return word[:2]


if __name__ == '__main__':
    symbols = "Hi He Lied Because Boron Could Not Oxidize Fluorine." \
              " New Nations Might Also Sign Peace Security Clause. Arthur King Can."

    words = symbols.split(" ")
    one_letters = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    elements = []

    for i, word in enumerate(words, start=1):
        elements.append(get_element(i, word))

    print({i: el for i, el in enumerate(elements)})
