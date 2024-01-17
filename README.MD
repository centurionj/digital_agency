python3 -m venv venv

source venv/bin/activate

cd scr/

pip install -r requirements.txt

python manage.py collectstatic

python manage.py runserver

шаблоны https://silicon.createx.studio/landing-digital-agency.html