#!/usr/bin/env bash
# sets up web server for the deployment of web static
apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" | tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/
FILE=/etc/nginx/sites-available/default
sed -i '30i\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\\
n\t}\n' $FILE
service nginx restart
