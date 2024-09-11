#!/bin/bash

# # Change directory to blockchain
cd ./blockchain

# Install missing npm packages
npm install npm-install-missing
npm install solc@0.5.0

# Install all npm packages
npm install

# Run ganache-cli in the background and log output to ganache.log
nohup ganache-cli --port 7545 --hostname 0.0.0.0 --gasLimit 8000000 --mnemonic "transcendence" &> ganache.log &
sleep 5
node scripts/deploy.js | grep "0x" | cut -c 31- > /app/data/contractAddress.txt

# Keep the script running
tail -f /dev/null