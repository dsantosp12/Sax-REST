#!/usr/bin/env bash

sudo apt install python3
sudo apt install python3-pip
sudo apt install sqlite3

mkdir -p "$HOME/.config/sax/"
sudo mkdir -p /usr/local/sax/sax-rest

# Setup project
sudo cp -r ./* /usr/local/sax/sax-rest

sudo python3 /usr/local/sax/sax-rest/setup.py install

# Copy service file
sudo cp sax-rest /etc/init.d

echo "
[Unit]
Description=Sax REST is the API for other services

[Service]
Type=simple
WorkingDirectory=/usr/local/sax/sax-rest
User=sax
Group=sax
ExecStart=/usr/local/sax/sax-rest/run
ExecStop=kill `cat /var/run/sax-rest.pid`
Restart=always
SyslogIdentifier=sax

" > /etc/init/sax-rest.service
