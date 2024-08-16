# Use an appropriate base image
FROM ubuntu:latest

# Update and upgrade packages
RUN apt-get update -y && apt-get upgrade -y

# Set the working directory
WORKDIR /app

# Configure SSH and root password
RUN echo 'root:12345' | chpasswd
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN ssh-keygen -A

# Install Python and dependencies
RUN apt-get install -y python3 python3-pip
ENV PIP_BREAK_SYSTEM_PACKAGES=1
RUN pip3 install django djangorestframework django-cors-headers djangorestframework-simplejwt django-extensions pyOpenSSL Werkzeug

# Install Solidity Web3 Module
RUN pip3 install web3==5.25.0

# Install PostgreSQL and dependencies
RUN apt-get install -y python3-psycopg2 postgresql postgresql-contrib sudo

# Copy scripts and configuration files
COPY ./script/script.sh ./script.sh
COPY ./files/pg_hba.conf ./pg_hba.conf
# COPY ./transcendence ./transcendence

# Set permissions for the script
RUN chmod +x /app/script.sh

# Set PostgreSQL password
RUN echo 'postgres:12345' | chpasswd

# Allow root to run commands as postgres user without password
RUN echo 'root ALL=(postgres) NOPASSWD: ALL' >> /etc/sudoers

# Expose the application port
EXPOSE 8000

# Node.js and Solidity dependencies
RUN apt-get install -y curl

# Install nvm and Node.js
ENV NVM_DIR=/usr/local/nvm
ENV NODE_VERSION=22.4.1
RUN mkdir -p $NVM_DIR
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
RUN . $NVM_DIR/nvm.sh && nvm install $NODE_VERSION && nvm use $NODE_VERSION && nvm alias default $NODE_VERSION
ENV PATH=$NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH
RUN apt-get install npm -y

# Install npm packages globally
RUN npm install -g truffle ganache-cli

# Copy blockchain files and compile contracts
COPY ./blockchain /app/blockchain
RUN cd /app/blockchain && truffle compile
COPY ./transcendence ./transcendence

# Set the entrypoint for the container
ENTRYPOINT ["/app/script.sh"]
