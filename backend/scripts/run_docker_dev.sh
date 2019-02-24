#!/bin/bash
ls
scripts/wait-for-it.sh localhost:5432 -t 20
python iamsitting_site/manage.py makemigrations
python iamsitting_site/manage.py migrate
python iamsitting_site/manage.py runserver
