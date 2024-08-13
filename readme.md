python3 -m venv venv        
. venv/bin/activate 


pip install django

django-admin startproject custom_admin .


python manage.py runserver


separate TERMINAL 

python manage.py migrate

python manage.py createsuperuser