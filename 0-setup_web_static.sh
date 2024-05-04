#!/usr/bin/env bash
# script to set up web servers for deployment of web_static

# install nginx if not installed
if ! which nginx >/dev/null 2>&1; then
	echo "Installing Nginx..."
	sudo apt-get update -y
	sudo apt-get install nginx -y
fi

# create folder if it doesn't exist
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo touch /data/web_static/releases/test/index.html

# set ownership of folder
sudo chown -R ubuntu:ubuntu /data

sudo echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link (delete existing if present)
if [ -L /data/web_static/current ]; then
	echo "Removing existing symbolic link..."
	sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current

# check if the config exsits before adding
# if ! grep -q "location /hbnb_static" /etc/nginx/sites-available/default; then
# 	sudo sed -i '/add_header X-Served-By \$hostname;/a \\n\t location /hbnb_static \n\t{\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default
# fi
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/; }' /etc/nginx/sites-enabled/default
sudo service nginx restart
