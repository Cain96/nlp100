#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k9.py
import random

if __name__ == '__main__':
    def change_word(word: str):
        if len(word) > 4:
            num = len(word)
            return word[0] + "".join(random.sample(word[1:num - 1], num - 2)) + word[-1]
        return word

    str = "I couldn't believe that I could actually understand what I was reading :" \
          " the phenomenal power of the human mind ."
    str_list = [change_word(word) for word in str.split(" ")]
    print(" ".join(str_list))
