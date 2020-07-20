#!/usr/bin/env bash

cd /home/cbaxter/build/lcg

docker build -f build.Dockerfile -t cbaxter1988/lcg .

docker-compose up -d

rm -rf /home/cbaxter/build/lcg