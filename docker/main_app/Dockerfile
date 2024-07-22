FROM ubuntu:latest

RUN apt-get upgrade -y && apt-get update -y

WORKDIR /app

RUN echo 'root:12345' | chpasswd
RUN apt-get install openssh-server -y
RUN ssh-keygen -q -t rsa -N '' -f /id_rsa

RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

ENV PIP_BREAK_SYSTEM_PACKAGES 1

# Installations for Main App

RUN pip3 install django
RUN pip3 install djangorestframework
RUN pip3 install django-cors-headers
RUN pip3 install djangorestframework-simplejwt
RUN pip3 install django-extensions
RUN pip3 install pyOpenSSL
RUN apt-get install python3-psycopg2 -y
RUN pip install Werkzeug
RUN apt-get install sudo

RUN apt-get install postgresql -y

# Installations for Solidity

RUN apt install nodejs npm

RUN npm install -g truffle
RUN npm install -g ganache-cli

RUN mkdir transcendence_blockchain
RUN cd transcendence_blockchain

RUN truffle compile

RUN cd /app

# END

COPY ./script/script.sh script.sh
COPY ./files/pg_hba.conf .
COPY ./transcendence ./transcendence

RUN chmod +x ./script.sh

RUN echo 'postgres:12345' | chpasswd

RUN echo 'root ALL=(postgres) NOPASSWD: ALL' >> /etc/sudoers

EXPOSE 8000

ENTRYPOINT ["./script.sh"]
