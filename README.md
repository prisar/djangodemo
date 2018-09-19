## Development:
Access application from 'https://djangodemo-pritimay.c9users.io/' and the admin page from 
'https://djangodemo-pritimay.c9users.io/admin'.

## Deployment:
https://vast-taiga-70981.herokuapp.com/

## Steps to setup and deploy in heroku

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    `$ python manage.py migrate`

2) Run Django

    `$ python manage.py runserver $IP:$PORT`

3) Create superuser for with admin role for the application

    `python manage.py createsuperuser`

4) Install postgres using

    `sudo apt-get update`
    
    `sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib`

5) Make migrations

    `python manage.py makemigrations`

6) Install psycopg2

    `sudo pip install psycopg2`


7) Create Database

    `CREATE DATABASE djangodemo;`

8) Create database user to connect and interact with database

    `CREATE USER djangodemouser WITH PASSWORD 'password';`

9) Add encoding, trasaction scheme and timezone

    `ALTER ROLE myprojectuser SET client_encoding TO 'utf8';`
    `ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';`
    `ALTER ROLE myprojectuser SET timezone TO 'UTC';`

10) Give user rights to the create database

    `GRANT ALL PRIVILEGES ON DATABASE djangodemo TO djangodemouser;`

11) Postgre shell

    `$ sudo su - postgres`

12) Run Sql query

    `$ psql -h localhost -d djangodemo -U djangodemouser -W`

13) Exit sql prompt

    `\q`

14) Exit out of postgres shell

    `exit`

15) Add app issues

    `$ python manage.py startapp issues`

16) Start postgres

    `$ sudo service postgresql start`

17) Start postgres at boot

    `$ sudo update-rc.d postgresql enable`

18) Install rest_framework 3.6.4 since >=3.7 is not supported for django 1.9

    `$ sudo pip install rest_framework==3.6.4`

19) Deployment in heroku. Login first, and then

    `heroku create`

20) Heroku `DISABLE_COLLECSTATIC` using

    `$ heroku config:set DISABLE_COLLECTSTATIC=1`

21) Add Procfile and `web: gunicorn djangodemo.wsgi`

22) Add requirements.txt file

    `pip freeze > requirements.txt`

23) Add `django-heroku` and `gunicorn` 

24) Write in settings file 

    `import django_heroku`
    `django_heroku.settings(locals())`

25) Heroku url

    https://vast-taiga-70981.herokuapp.com/

26) Push db

    `heroku pg:push djangodemo DATABASE_URL --app vast-taiga-70981`

27) Connect db

    `heroku pg:psql`


28) Export db url

    `export DATABASE_URL=postgres://$(whoami)`
