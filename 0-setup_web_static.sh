#!/bin/bash
#Setup the webserver for deployement
apt update -y
apt install nginx -y
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<h1>Test me</h1>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -Rh ubuntu:ubuntu /data/
sed -i.bak '/^server {$/a\\t location /hbnb_static {\n\t\talias /data/web_static/current;\n}' /etc/nginx/sites-available/default
service nginx restart