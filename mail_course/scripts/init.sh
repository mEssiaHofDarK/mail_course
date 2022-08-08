#!/bin/bash

echo "creating working tree ..."
mkdir -p /home/box/web/{public,uploads,etc} /home/box/web/public/{img,css,js}
echo "working tree created! coping nginx.conf ..."
cp /home/box/mail_course/mail_course/nginx/nginx.conf /home/box/web/etc
echo "nginx.conf copied! creating config link ..."
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
echo "link created! restarting nginx ..."
service nginx restart
echo "init complete!"
#if [[ $(systemctl is-enabled nginx) == "enabled" ]]; then
#  service nginx restart
#else
#  service nginx start
#fi




