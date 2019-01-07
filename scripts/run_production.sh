#!/bin/bash 

cd ..
source ~/Envs/djenv/bin/activate
sudo service gunicorn stop
git stash
git pull
pip install -r requirements/production.txt
iamsitting_site/manage.py makemigrations
iamsitting_site/manage.py migrate
npm install
npm run build
iamsitting_site/manage.py collectstatic
sudo service gunicorn start

