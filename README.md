# pmdb

# INSTALATION:

virtualenv -p python3 pmdb_venv
cd pmdb_venv
source bin/activate
git clone https://github.com/admed/pmdb
cd pmdb/
pip install -r requirements.txt
pip install -r requirements_dev.txt
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
