#!/bin/bash

echo "Deploy stage"

scp docker-compose.yaml jenkins@swarm-manager-2:/home/jenkins/docker-compose.yaml
ssh jenkins@swarm-manager-2 \
DOCKER_HUB_CREDS_USR=$DOCKER_HUB_CREDS_USR \
CREATE_SCHEMA=true \
DATABASE_URI=$DATABASE_URI \
docker stack deploy --compose-file docker-compose.yaml DFE-project