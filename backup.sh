#!/bin/bash

name=your-container-name

id=$(docker ps -a | grep $name | head -n 1 | awk {'print $1'})

sudo docker cp $id:/bot/data/blacklist.json data/blacklist.json
sudo docker cp $id:/bot/data/haregly.json data/haregly.json
