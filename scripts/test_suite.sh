#!/usr/bin/env bash

export DJANGO_SETTING_MODULE=ap.settings.development

echo "Loading webpack ... ..."
npm run dev > run_webpack.log 2>&1 &
WEBPACK_PID=$!
sleep 2
while ! grep -qw "Compiled successfully." run_webpack.log; do sleep 5; done

echo "Loading Django ... ..."
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

