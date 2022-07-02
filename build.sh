#!/bin/bash

VERSION="1"
docker login
docker build -t ashspiker/rest-service:${VERSION} .
docker push ashspiker/rest-service:${VERSION}