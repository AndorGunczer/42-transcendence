#!/bin/bash

mkdir ssl

cd ssl

openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365
openssl x509 -outform der -in cert.pem -out cert.crt

service postgresql start
sleep 10

# psql -c "CREATE USER project WITH PASSWORD '12345';"
# psql -c "CREATE DATABASE transcendence;"
# psql -c "ALTER DATABASE transcendence OWNER TO project;"

sudo -u postgres psql template1 -c "ALTER USER postgres WITH ENCRYPTED PASSWORD '12345';"
cp /app/pg_hba.conf /etc/postgresql/16/main/pg_hba.conf

service postgresql restart

psql -v ON_ERROR_STOP=1 --username "postgres" <<-EOSQL
    CREATE USER project WITH PASSWORD '12345';
    CREATE DATABASE transcendence;
    ALTER DATABASE transcendence OWNER TO project;
EOSQL

# # Change directory to blockchain
cd ../blockchain

# Install missing npm packages
npm install npm-install-missing
npm install solc@0.5.0

# Install all npm packages
npm install

# Run ganache-cli in the background and log output to ganache.log
nohup ganache-cli --port 7545 --hostname 127.0.0.1 --gasLimit 8000000 --mnemonic "transcendence" &> ganache.log &
sleep 5
node scripts/deploy.js | grep "0x" | cut -c 31- > /app/contractAddress.txt

# Change the directory to transcendence

cd ../transcendence

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py populate_avatars

# Run Django server in the background
nohup python3 manage.py runserver_plus 0.0.0.0:8000 --cert-file /app/cert.crt --key-file /app/key.pem &


# Keep the script running
tail -f /dev/null
