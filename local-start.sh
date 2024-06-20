#!/usr/bin/env bash

trap 'kill $(jobs -p)' EXIT

set -e
set -x

source /Users/gillian/.pyenv/versions/car/bin/activate

cd client
npm i
npm run build

cd ../node-server
npm i
npm run build

npm start
&
python ../python/move_receiver.py

wait
