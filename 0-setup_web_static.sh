#!/usr/bin/env bash
# sets up web server for the deployment of web static
apt-get update
apt-get install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
ln -s /data/web_static/current /data/web_static/releases/test/
chmod -R 770 /data/
FILE=/etc/nginx/sites-available/default
sed -i '30i\\n\tlocation /hbnb_static/ {\n\t\talias https://mydomainname.tech/h\
bnb_static/;\n\t}' $FILE
service nginx restart
