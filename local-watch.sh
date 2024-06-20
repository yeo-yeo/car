#!/usr/bin/env bash

trap 'kill $(jobs -p)' EXIT

set -e
set -x

# source /Users/gillian/.pyenv/versions/car/bin/activate

# echo "😀"
# echo $(pip list)

npm run watch --prefix client &
npm run watch --prefix node-server

# y u no work
# &
# ../python/move_receiver.py

wait
