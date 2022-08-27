#!/bin/bash

echo "coping project ..."
mkdir web
mv /home/box/mail_course/mail_course/web/* ~/web/*
echo "coping complete! configure nginx and restart..."
sudo ln -f /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
echo "run gunicorn ..."
gunicorn -c /home/box/web/etc/gunicorn_django_config.py ask.wsgi:application &
echo "init complete!"
