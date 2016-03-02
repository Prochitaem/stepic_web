echo "Creating directories..."
cd /home/box/web
mkdir public
mkdir uploads
mkdir etc
cd public
mkdir img
mkdir css
mkdir js
echo "Directories created!"
sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf