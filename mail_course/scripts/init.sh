#!/bin/bash

mkdir -p /home/box/web/{public,uploads,etc} /home/box/web/public/{img,css,js}
cp /home/box/mail_cource/nginx/nginx.conf /home/box/web/etc
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
if [[ $(systemctl is-enabled nginx) == "enabled" ]]; then
  service nginx restart
else
  service nginx start
fi




