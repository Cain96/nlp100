import gzip
import json

from pymongo import MongoClient


def open_gzip(filename="../data/artist.json.gz"):
    with gzip.open(filename, 'rt') as lines:
        for line in lines:
            artist = json.loads(line)
            yield artist


def mongo_connect():
    return MongoClient('localhost', 27017).testdb.artist
