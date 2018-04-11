#!/usr/bin/env python
# -*- coding: utf-8 -*-
# k59.py
from xml.etree import ElementTree as ET


def token_parse(string: str):
    return read(tokenize(string))


def tokenize(string: str):
    return string.strip().replace('(', '( ').replace(')', ' )').split()


def read(tokens: list):
    if not tokens:
        return None

    token = tokens.pop(0)
    if token == "(":
        list = []
        while tokens[0] != ")":
            token = read(tokens)
            if token is not None:
                list.append(token)
        tokens.pop(0)
        return list
    else:
        return token


def is_pair(tokens: list):
    return all([isinstance(tokens, list), isinstance(tokens[0], str), isinstance(tokens[-1], str)])


def output_words(token_list: list):
    if is_pair(token_list):
        return token_list[-1]
    return " ".join(map(output_words, token_list[1:]))


def evaluate(token_list: list):
    if token_list[0] == 'NP':
        print(output_words(token_list))
    for token in token_list[1:]:
        if not is_pair(token):
            evaluate(token)


if __name__ == '__main__':
    filename = "../data/nlp.txt.xml"
    root = ET.parse(filename)

    for parse in root.iterfind('./document/sentences/sentence/parse'):
        parsed_list = token_parse(parse.text)
        evaluate(parsed_list)
