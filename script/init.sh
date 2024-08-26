#!/bin/bash

#script for development on mac

# copying files and keys when the app is installed anew
# but all prerequsites were already installed and the db exists

mkdir app
cp -r blockchain app
cp -r transcendence app
cp  script.sh app


cd app

mkdir ssl
cd ssl

openssl req -x509 -nodes -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365
openssl x509 -outform der -in cert.pem -out cert.crt

# in web3_utils.py
# /Users/mrubina/projects/transcendence/tr2/app/contractAddress.txt
# 
