#!/bin/bash

cd ssl

# openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365
# openssl x509 -outform der -in cert.pem -out cert.crt

openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout private.key -out selfsigned.crt \
  -subj "/C=AU/ST=Some-State/L=City/O=Internet Widgits Pty Ltd/OU=Section/CN=localhost/emailAddress=email@example.com"


service postgresql start
sleep 10

# psql -c "CREATE USER project WITH PASSWORD '12345';"
# psql -c "CREATE DATABASE transcendence;"
# psql -c "ALTER DATABASE transcendence OWNER TO project;"
export PGPASSWORD='12345'

sudo -u postgres psql template1 -c "ALTER USER postgres WITH ENCRYPTED PASSWORD '12345';"
cp /app/pg_hba.conf /etc/postgresql/16/main/pg_hba.conf

service postgresql restart

psql -v ON_ERROR_STOP=1 --username "postgres" <<-EOSQL
    CREATE USER project WITH PASSWORD '12345';
    CREATE DATABASE transcendence;
    ALTER DATABASE transcendence OWNER TO project;
EOSQL

# Change the directory to transcendence

cd ../transcendence

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py populate_avatars
service nginx start

# Run Django server in the background # nohup
daphne -p 8000 transcendence.asgi:application

# Keep the script running
tail -f /dev/null
