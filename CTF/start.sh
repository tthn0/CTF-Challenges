#!/bin/bash

if [ -z "$1" ]; then
  echo "An argument is required."
elif [ "$1" -eq 1 ]; then
  export NODE_ENV=development
  docker compose up --build --watch
  docker compose down --volumes --remove-orphans
elif [ "$1" -eq 2 ]; then
  export NODE_ENV=production
  chmod -R a+w ./log
  docker compose up --build -d
else
  echo "Invalid argument."
fi