#!/usr/bin/env bash

# Check if Python 3 is installed
if command -v python3; then
    echo "Python3 found"
else
    >&2 echo "Python3 is required. Install with sudo apt install python3"
    exit 1
fi

# Check for pip3
if command -v pip3; then
    echo "Pip3 found"
else
    >&2 echo "Pip3 is required. Install with sudo apt install python3-pip"
    exit 1
fi

# Check for Sqlite3
if command -v sqlite3; then
    echo "Sqlite3 found"
else
    >&2 echo "Sqlite3 is required. Install with sudo apt install sqlite3"
fi

# Check for virtualenv
if command -v virtualenv; then
    echo "Virtualenv found"
else
    >&2 echo "Virtualenv is required. Install with sudo apt install virtualenv"
fi

# Check for pwgen
if command -v pwgen; then
    echo "pwgen found"
else
    apt install pwgen
fi

mkdir -p /usr/local/sax/sax-rest

# Setup project
cp -r ./* /usr/local/sax/sax-rest
virtualenv /usr/local/sax/venv/ --python=python3

# Install dependencies to environment
source /usr/local/sax/venv/bin/activate
pip3 install -r /usr/local/sax/sax-rest/requirements.txt
deactivate

# Copy service file
cp sax-rest /etc/init.d
chmod +x /etc/init.d/sax-rest

systemctl daemon-reload

export SAX_TOKEN_AUTH=`pwgen 40 1`

echo ""
echo "************************************************************************"
echo "Authorization Token: $SAX_TOKEN_AUTH"
echo "************************************************************************"
echo ""
echo "Export this permanently in SAX_TOKEN_AUTH"
echo ""
echo "Installed successfully"