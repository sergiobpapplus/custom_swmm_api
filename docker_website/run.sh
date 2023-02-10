#!/usr/bin/env bash
docker run -p5100:5100 -it --volume $PWD/.:/home/mp --user $(id -u):$(id -g) registry.gitlab.com/markuspichler/swmm_api:latest /bin/bash