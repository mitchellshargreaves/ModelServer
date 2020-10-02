#!/bin/bash
app="fastapi-pytorch"

# Remove this once testing is complete
docker stop ${app}
docker rm ${app}

docker build -t ${app} .
docker run -p 80:80 \
  --name=${app} \
  -v $PWD:/app ${app}
