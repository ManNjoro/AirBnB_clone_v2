#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "Nginx successful" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
echo "server {
    listen 80;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html;
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=SlxFYguZxm8;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
	location /hbnb_static {
		alias /data/web_static/current/
	}
}" | sudo tee /etc/nginx/sites-available/default
sudo service nginx restart
