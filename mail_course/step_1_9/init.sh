#!/bin/bash

echo "coping project ..."
mv /home/box/mail_course/mail_course/step_1_9/* ~
echo "coping complete! configure nginx and restart..."
sudo ln -f /home/box/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
echo "configure gunicorn and restart..."
sudo ln -f /home/box/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
echo "init complete!"
