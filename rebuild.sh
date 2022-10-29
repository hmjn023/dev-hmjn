#!/bin/sh

# remove old container
docker stop gionsai
docker rm gionsai
docker image rm gionsai

# build and create new container
docker build -t gionsai ./docker
docker run -p 18526:18526 -d --name "gionsai" gionsai
