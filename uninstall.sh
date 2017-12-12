#!/usr/bin/env bash

service sax-rest stop

rm -rf "$HOME/.config/sax"
rm -rf /usr/local/sax/sax-rest
rm -rf /etc/init.d/sax-rest

systemctl daemon-reload