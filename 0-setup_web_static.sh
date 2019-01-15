#!/usr/bin/env bash
# sets up web server for the deployment of web static
apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
FILEA=/data/web_static/current
rm -rf /data/web_static/releases/test/current
if [ -L $FILEA ]; then
    rm -rf /data/web_static/current
fi
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
chmod -R 755 /data/
FILE=/etc/nginx/sites-available/default
sed -i '30i\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\
n\t}\n' $FILE
service nginx restart
