#!/usr/bin/env bash

apt install python3
apt install python3-pip
apt install sqlite3

mkdir -p "$HOME/.config/sax/"
mkdir -p /usr/local/sax/sax-rest

# Setup project
cp -r ./* /usr/local/sax/sax-rest

# Copy service file
cp sax-rest /etc/init.d

echo "
[Unit]
Description=Sax REST is the API for other services

[Service]
Type=simple
WorkingDirectory=/usr/local/sax/sax-rest
User=sax
Group=sax
ExecStart=/usr/local/sax/sax-rest/run
ExecStop=kill \`cat /var/run/sax-rest.pid\`
Restart=always
SyslogIdentifier=sax

" > /etc/systemd/user/sax-rest.service
