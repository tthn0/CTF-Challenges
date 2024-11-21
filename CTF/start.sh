#!/bin/bash

if [ -z "$1" ]; then
  echo "An argument is required."
elif [ "$1" -eq 1 ]; then
  npm ci
  npm start
elif [ "$1" -eq 2 ]; then
  export ENV=development
  docker compose up --build
  docker compose rm -fsv
elif [ "$1" -eq 3 ]; then
  export ENV=production
  docker compose up --build -d
else
  echo "Invalid argument."
fi
