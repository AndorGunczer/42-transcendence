FROM ubuntu:latest

RUN apt-get upgrade -y && apt-get update -y

WORKDIR /app

RUN echo 'root:12345' | chpasswd
RUN apt-get install openssh-server -y
RUN ssh-keygen -q -t rsa -N '' -f /id_rsa

RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

ENV PIP_BREAK_SYSTEM_PACKAGES 1

RUN apt update
RUN apt install nodejs npm

RUN npm install -g truffle
RUN npm install -g ganache-cli

RUN mkdir transcendence
RUN cd transcendence

RUN truffle compile

# RUN cd contracts
# RUN touch Tournaments.sol

