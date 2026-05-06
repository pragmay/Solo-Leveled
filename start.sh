#!/bin/bash
sudo service mariadb start
sudo mysqladmin -u root -pJames_Bond status 2>/dev/null || sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED BY 'James_Bond'; FLUSH PRIVILEGES;"
/usr/local/bin/python3 -m pip install mysql-connector-python ipykernel --quiet
/usr/local/bin/python3 -m ipykernel install --user --name python3 --display-name "Python 3.12"
echo "✅ Ready!"