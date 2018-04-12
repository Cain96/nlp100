#!/usr/bin/env bash
mongo testdb << EOF
db.artist.find({ name: 'Queen' })
EOF