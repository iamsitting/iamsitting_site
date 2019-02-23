#!/bin/bash 

cd ..
source ~/Envs/djenv/bin/activate
sudo service gunicorn stop
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

