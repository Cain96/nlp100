#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k37.py

from collections import Counter

from chap4.utils import morphological
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic'

if __name__ == '__main__':
    counter = Counter()

    for sentence in morphological():
        counter.update([word['surface'] for word in sentence])

    freqs = counter.most_common(10)

    x = range(10)
    y = [freq[1] for freq in freqs]
    label = [freq[0] for freq in freqs]

    plt.bar(x, y, tick_label=label)
    plt.show()
