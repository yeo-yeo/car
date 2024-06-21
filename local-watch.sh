#!/usr/bin/env bash

trap 'kill $(jobs -p)' EXIT

set -e
set -x

source /Users/gillian/.pyenv/versions/car/bin/activate

npm run watch --prefix client &
npm run watch --prefix node-server &
./python/move_receiver.py

wait
