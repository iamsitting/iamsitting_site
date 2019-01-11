#!/usr/bin/env bash

export DJANGO_SETTINGS_MODULE=iamsitting_site.settings.travis

echo "Loading webpack ... ..."
npm run dev > run_webpack.log 2>&1 &
WEBPACK_PID=$!
sleep 2
while ! grep -qw "Compiled successfully." run_webpack.log; do sleep 5; done
echo 'Webpack server successfully started.'

echo "Loading Django ... ..."
python iamsitting_site/manage.py runserver &
DJANGO_PID=$!
sleep 10
echo 'Hopefully Django server successfully started.'

echo "testing Django ... ..."
python iamsitting_site/manage.py test --verbosity=2


echo "killing processes"
kill -INT $WEBPACK_PID
kill -INT $DJANGO_PID
echo "test suite finished"

