cd /root/reinspy;
git pull;
mkdocs build;
cp -fR site* /var/www/reinspy.com/docs;