#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Invalid args"
  exit 1
fi

mkdir chap$1
cd chap$1

let max=$1*10-1
let min=$max-9

for i in `seq $min $max`; do
    echo "#!/usr/bin/env python" > k$i.py
    echo "# -*- coding: utf-8 -*-" >> k$i.py
    echo "# k${i}.py" >> k$i.py
done;
exit 0
