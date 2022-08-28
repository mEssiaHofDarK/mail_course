#!/bin/bash

echo "coping project ..."
mkdir web
mv /home/box/mail_course/mail_course/web/* ~/web/

echo "start mysql server..."
sudo /etc/init.d/mysql start

echo "create db 'ask' and django models..."
mysql -u root -e "create database if not exists ask character set utf8;"
mysql -u root -e "grant all privileges on ask.* to 'box'@'localhost' with grant option;"
python3 web/ask/manage.py makemigrations qa
python3 web/aks/manage.py migrate qa

echo "configure nginx..."
sudo ln -f /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

echo "run gunicorn ..."
gunicorn -c /home/box/web/etc/gunicorn_django_config.py ask.wsgi:application &

echo "init complete!"
