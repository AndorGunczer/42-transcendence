#!/bin/bash

cd blockchain

npm install npm-install-missing

npm install

nohup ganache-cli --port 7545 --hostname 127.0.0.1 --gasLimit 8000000 --mnemonic "transcendence" &> ganache.log &

