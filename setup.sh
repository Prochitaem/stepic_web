echo "Creating infrusructure..."
sudo ﻿ln -s /home/box/web/etc/test.conf  /etc/nginx/sites-enabled/test.conf
nginx -s reload
