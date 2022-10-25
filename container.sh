#!/bin/sh
docker build -t gionsai ./docker

docker run -p 18526:18526 -d --name "gionsai" gionsai
