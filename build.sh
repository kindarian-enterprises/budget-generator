#!/bin/bash


if [ -z "$BUILD_TAG" ];
  then
    echo "\$BUILD_TAG is not defined, defaulting to 'latest'"
    BUILD_TAG=latest
fi

if [ -z "$DOCKER_USERNAME" ];
  then
    echo "\$DOCKER_USERNAME is not defined, cannot complete build."
    exit 1
fi

if [ -z "$DOCKER_PASSWORD" ];
  then
    echo "\$DOCKER_PASSWORD is not defined, cannot complete build."
    exit 1
fi

IMAGE_NAME=$DOCKER_USERNAME/budget-generator:$BUILD_TAG

docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD

docker build -f nginx_uwsgi_dockerfile -t $IMAGE_NAME .

docker push $IMAGE_NAME
