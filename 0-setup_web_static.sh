<<<<<<< HEAD
#!/bin/bash/env bash
# This script sets up a eb server for the deployment of web_static
# it Install Nginx if it not already installed, creates the needed folders, a symbolic link
# gives ownership of the /data/ folder to ubuntu user and group.

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i `/listen 80 desault_server/a location /hbnh_static { alias /data/web_static/current/;}` /etc/nginx/sites-enabled/default

sudo service nginx restart
=======
#!/usr/bin/env bash
# bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
sudo echo "<p>Hello Worldddd!</p>" | sudo tee /data/web_static/releases/test/index.html

# Remove existing symbolic link if it exists
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi

sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '53i \\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
/etc/init.d/nginx restart
>>>>>>> 04c146b1529a4df5fc0a55a99ebb1fb3510386f1
