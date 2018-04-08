#!/usr/bin/env bash
grep "^する\s" ../data/45.txt | sort | uniq -c | sort -r
grep "^見る\s" ../data/45.txt | sort | uniq -c | sort -r
grep "^与える\s" ../data/45.txt | sort | uniq -c | sort -r