#!/usr/bin/env bash
mongo testdb << EOF
db.artist.find({ area: 'Japan' }).count()
EOF