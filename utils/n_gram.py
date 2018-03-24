#!/usr/bin/env python
# -*- coding: utf-8 -*-

class N_Gram():
    def n_gram(self, text, num):
        return ["".join(text[i:i + num]) for i in range(len(text) - (num - 1))]

    def bi_gram(self, text):
        return self.n_gram(text, 2)
