#!/usr/bin/env bash
cut -f1,2 ../data/47.txt | sort | uniq -c | sort -r