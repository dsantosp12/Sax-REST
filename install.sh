#!/usr/bin/env bash

sudo apt install python3
sudo apt install pip3
sudo apt install sqlite3

mkdir "$HOME/.config/sax/"
sudo mkdir -p /usr/local/sax/sax-rest

# Copy service file
sudo cp sax-rest /etc/init.d

# Setup project
sudo cp -r ./* /usr/local/sax/sax-rest

python3 /usr/local/sax/sax-rest/setup.py install
