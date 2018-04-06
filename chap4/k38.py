#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k38.py
from collections import Counter

from chap4.utils import morphological
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic'

if __name__ == '__main__':
    counter = Counter()

    for sentence in morphological():
        counter.update([word['surface'] for word in sentence])

    freqs = sorted(counter.most_common(), key=lambda x: (-x[1], x[0]))

    x = [freq[1] for freq in freqs]

    plt.hist(x, bins=30, range=(1, 30))
    plt.xlim(xmin=1, xmax=30)
    plt.show()
