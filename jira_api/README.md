Create the virtual environment -> python -m venv env
Activate the virtual environment	source env/bin/activate
Install Django	python -m pip install django
Pin your dependencies	python -m pip freeze > requirements.txt
Set up a Django project	django-admin startproject <projectname>
Start a Django app	python manage.py startapp <appname>

To run the server  python manage.py runserver
create the migrations -> python manage.py makemigrations
migrate -> python manage.py migrate
