#!/usr/bin/env bash
docker build -t registry.gitlab.com/markuspichler/swmm_api:latest . --platform=linux/amd64

docker build -t registry.gitlab.com/markuspichler/swmm_api:2023-03-10 .