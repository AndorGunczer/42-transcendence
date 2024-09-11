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

# Install Solidity Web3 Module
RUN pip3 install web3

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



# Copy files
COPY ./application /app/blockchain
RUN cd /app/blockchain && truffle compile
COPY ./script/script.sh /app/script.sh

# Set permissions for the script
RUN chmod +x /app/script.sh

# Set the entrypoint for the container
ENTRYPOINT ["/app/script.sh"]
