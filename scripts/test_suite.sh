#!/usr/bin/env bash

cd iamsitting_site

export DJANGO_SETTINGS_MODULE=iamsitting_site.settings.travis

echo "Loading webpack ... ..."
npm run dev > run_webpack.log 2>&1 &
WEBPACK_PID=$!
sleep 2
while ! grep -qw "Compiled successfully." run_webpack.log; do sleep 5; done

echo "Loading Django ... ..."
python manage.py makemigrations
python manage.py migrate
python manage.py runserver &
DJANGO_PID=$!
sleep 2

echo "testing Django ... ..."
python manage.py test --verbosity=2
sleep 2

echo "killing processes"
kill -INT $WEBPACK_PID
kill -INT $DJANGO_PID
echo "test suite finished"

