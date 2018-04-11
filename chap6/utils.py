import re

from nltk import stem


def get_lines(filename="../data/nlp.txt"):
    pattern = re.compile("(^.*?[\.|;|:\?|!])\s([A-Z].*)$")
    with open(filename) as lines:
        for line in lines:
            line = line.strip()
            while line:
                m = pattern.match(line)
                if m:
                    yield m.group(1)
                    line = m.group(2)
                else:
                    yield line
                    line = ''


def get_words():
    for line in get_lines():
        for word in line.split():
            yield word.rstrip('.,:?!')
        yield ""


def stemming(words):
    stemmer = stem.PorterStemmer()
    return [[word, stemmer.stem(word)] for word in words]


class Mention:
    def __init__(self, start, end, text, representative):
        self.start = start
        self.end = end
        self.text = text
        self.representative = representative
