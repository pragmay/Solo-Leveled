#!/bin/bash
sudo service mariadb start
sudo mysqladmin -u root -pJames_Bond status 2>/dev/null || sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED BY 'James_Bond'; FLUSH PRIVILEGES;"
pip install mysql-connector-python ipykernel --quiet
echo "✅ MariaDB and Python kernel ready!"