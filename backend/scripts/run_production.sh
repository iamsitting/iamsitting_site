#!/bin/bash

source ~/Envs/djenv/bin/activate
sudo service gunicorn stop
pg_dump iamsitting_site -U iamsitting -h localhost > ~/backups/iamsitting_dump.sql
./dropbox_uploader.sh delete /iamsitting_dump.sql.old
./dropbox_uploader.sh move /iamsitting_dump.sql /iamsitting_dump.sql.old
./dropbox_uploader.sh upload ~/backups/iamsitting_dump.sql /
git stash
git pull
cd ..
pip install -r requirements/production.txt
mkdir iamsitting_site/logs
touch iamsitting_site/logs/feedback.log
touch iamsitting_site/logs/debug.log
python iamsitting_site/manage.py makemigrations
python iamsitting_site/manage.py migrate
cd ../frontend
npm install
npm run build
cd ../backend
python iamsitting_site/manage.py collectstatic
sudo service gunicorn start
