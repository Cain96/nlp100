import re


def morphological(filename="../data/neko.txt.mecab"):
    sentence_list = []
    sentence = []

    tab = re.compile("[,\t]")
    with open(filename) as lines:
        for line in lines:
            if line == "EOS\n":
                if len(sentence) > 0:
                    sentence_list.append(sentence)
                    sentence = []
            else:
                elements = tab.split(line.strip())
                word = {
                    "surface": elements[0],
                    "base": elements[7],
                    "pos": elements[1],
                    "pos1": elements[2]
                }
                sentence.append(word)
    return sentence_list


def n_gram(sentence, num):
    return [sentence[i:i + num] for i in range(len(sentence)) if i + num <= len(sentence)]
