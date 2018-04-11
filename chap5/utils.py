import re

import pydot


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return "surface:{}\tbase:{}\tpos:{}\tpos1:{}".format(self.surface, self.base, self.pos, self.pos1)


class Chunk:
    def __init__(self, dst=-1):
        self.morphs = []
        self.dst = dst
        self.srcs = []

    def __str__(self):
        return "{}\tsrcs:{}\tdst:{}".format(self.surface, self.srcs, self.dst)

    @property
    def surface(self):
        morphs = [morph for morph in self.morphs if morph.pos != "記号"]
        return "".join(map(lambda morph: morph.surface, morphs))

    @property
    def has_depend(self):
        return self.dst != -1

    def has_pos(self, pos):
        return any([morph.pos == pos for morph in self.morphs])

    def get_morphs_by_pos(self, pos):
        morphs = [morph for morph in self.morphs if morph.pos == pos]
        if morphs:
            return morphs[0]
        return ""

    def get_morphs_surfaces_by_pos(self, pos):
        return [(morph.base, self.surface) for morph in self.morphs if morph.pos == pos]

    @property
    def has_sahen_wo(self):
        return bool(self.get_sahen_wo())

    def get_sahen_wo(self):
        for i, morph in enumerate(self.morphs[:-1]):
            if morph.pos == "名詞" and morph.pos1 == "サ変接続":
                next_morph = self.morphs[i + 1]
                if next_morph.pos == "助詞" and next_morph.surface == "を":
                    return morph.surface + "を"
        return ""

    def path_to_root(self, sentence):
        return [self] + sentence[self.dst].path_to_root(sentence) if self.has_depend else [self]
        # path = []
        # chunk = self
        # while chunk.has_depend:
        #     path.append(chunk.surface)
        #     chunk = sentence[chunk.dst]
        # path.append(chunk.surface)
        # return path


def dependencies(filename="../data/neko.txt.cabocha"):
    exp = re.compile("^\*\s(?P<idx>\d+)\s(?P<dst>-?\d+)D")
    chunks = []
    chunk = Chunk()

    with open(filename) as lines:
        for line in lines:
            if line == "EOS\n":
                if chunk.morphs:
                    chunks.append(chunk)
                if chunks:
                    for i, chunk in enumerate(chunks):
                        if chunk.dst > -1:
                            chunks[chunk.dst].srcs.append(i)
                    yield chunks
                chunk = Chunk()
                chunks = []
            else:
                if line[0] == "*":
                    dst = int(exp.search(line).group('dst'))
                    if chunk.morphs:
                        chunks.append(chunk)
                    chunk = Chunk(dst)
                else:
                    line = line.replace("\t", ",")
                    values = line.split(",")
                    chunk.morphs.append(Morph(
                        values[0],
                        values[7],
                        values[1],
                        values[2]
                    ))
        raise StopIteration


def graph_from_edges(edges):
    graph = pydot.Dot(graph_type='digraph')

    for edge in edges:
        id1, label1, id2, label2 = str(edge[0][0]), str(edge[0][1]), str(edge[1][0]), str(edge[1][1])

        graph.add_node(pydot.Node(id1, label=label1))
        graph.add_node(pydot.Node(id2, label=label2))

        graph.add_edge(pydot.Edge(id1, id2))

    return graph


class Dependant:
    def __init__(self, predicate):
        self.subject = ""
        self.predicate = predicate
        self.object = ""

    def set_subject(self, subject):
        self.subject = subject

    def set_object(self, object):
        self.object = object

    def has_all_attribute(self):
        return all([bool(self.subject), bool(self.predicate), bool(self.object)])
