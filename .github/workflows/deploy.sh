#!/bin/sh

scp -r / SCP_USER@HOST:/var/www/html/
systemctl restart nginx
