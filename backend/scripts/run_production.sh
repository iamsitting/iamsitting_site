#!/bin/bash 

cd ..
source ~/Envs/djenv/bin/activate
sudo service gunicorn stop
pg_dump iamsitting_site -U iamsitting -h localhost > ~/backups/iamsitting_dump.sql
./dropbox_uploader.sh delete /iamsitting_dump.sql.old
./dropbox_uploader.sh move /iamsitting_dump.sql /iamsitting_dump.sql.old
./dropbox_uploader.sh upload ~/backups/iamsitting_dump.sql /
git stash
git pull
cd backend
pip install -r requirements/production.txt
iamsitting_site/manage.py makemigrations
iamsitting_site/manage.py migrate
cd ../frontend
npm install
npm run build
../backend/iamsitting_site/manage.py collectstatic
sudo service gunicorn start

