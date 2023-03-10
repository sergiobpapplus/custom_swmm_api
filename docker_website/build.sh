#!/usr/bin/env bash
docker build -t registry.gitlab.com/markuspichler/swmm_api:latest .

docker build -t registry.gitlab.com/markuspichler/swmm_api:2023-03-10 .