#!/usr/bin/env bash

export DJANGO_SETTINGS_MODULE=iamsitting_site.settings.travis

echo "Loading webpack ... ..."
cd frontend
npm run dev > run_webpack.log 2>&1 &
sleep 2
while ! grep -qw "Compiled successfully." run_webpack.log; do sleep 5; done
echo 'Webpack server successfully started.'

echo "Loading Django ... ..."
cd ../backend/iamsitting_site
python manage.py runserver &
sleep 10
echo 'Hopefully Django server successfully started.'

echo "testing Django ... ..."
cd iamsitting_site
python manage.py test --verbosity=2


echo "killing processes"
ps aux | grep webpack | awk '{print $2}' | xargs kill -9
ps aux | grep runserver | awk '{print $2}' | xargs kill -9
echo "test suite finished"

