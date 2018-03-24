#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k6.py
from utils.n_gram import N_Gram

if __name__ == '__main__':
    n = N_Gram()

    X = set(n.bi_gram(list("paraparaparadise")))
    Y = set(n.bi_gram(list("paragraph")))

    print("X:" + str(X))
    print("Y:" + str(Y))
    print("和集合:" + str(X | Y))
    print("積集合:" + str(X & Y))
    print("差集合(X-Y)" + str(X - Y))
    print("差集合(X-Y)" + str(Y - X))

    print("Xに'se'が含まれるか" + str('se' in X))
    print("Yに'se'が含まれるか" + str('se' in Y))
