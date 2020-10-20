#!/bin/bash

repo=('git@github.com:seraus09/site.git')

if [ -d "/home/site" ]
then
    cd /home/site && git pull $repo && docker-compose build && docker-compose up -d
else
    echo "Error: Directory does not exists."
fi
