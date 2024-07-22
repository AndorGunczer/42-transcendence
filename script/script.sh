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

cd ../transcendence

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver_plus 0.0.0.0:8000 --cert-file /app/cert.crt --key-file /app/key.pem

# tail -f /dev/null