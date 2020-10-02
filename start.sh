#!/bin/bash
app="fastapi-pytorch"
docker build -t ${app} .
docker run -p 80:80 \
  --name=${app} \
  -v $PWD:/app ${app}