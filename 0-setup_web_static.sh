#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static. It must:
# Install Nginx if not already installed
if ! [ -x "$(command -v nginx)" ]; then
    sudo apt update
    sudo apt install -y nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo tee /etc/nginx/sites-available/default >/dev/null <<EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
    }

    # Error pages
    error_page 404 /404.html;
    location = /404.html {
        root /usr/share/nginx/html;
        internal;
    }
}
EOF

# Restart Nginx to apply changes
sudo service nginx restart

# Exit successfully
exit 0

