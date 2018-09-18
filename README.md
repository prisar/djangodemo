You can access application from 'https://djangodemo-pritimay.c9users.io/' and the admin page from 
'https://djangodemo-pritimay.c9users.io/admin'.

## Starting from the Terminal

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    `$ python manage.py migrate`

2) Run Django

    `$ python manage.py runserver $IP:$PORT`
    
3) Postgre shell

    `$ sudo su - postgres`

4) Run Sql query

    `$ psql -h localhost -d djangodemo -U djangodemouser -W`

5) Add app issues

    `$ python manage.py startapp issues`

6) Start postgres

    `$ sudo service postgresql start`

7) Start postgres at boot

    `$ sudo update-rc.d postgresql enable`

8) Install rest_framework 3.6.4 since >=3.7 is not supported for django 1.9

    `$ sudo pip install rest_framework==3.6.4`

9) Heroku url

    https://vast-taiga-70981.herokuapp.com/

10) push db

    `heroku pg:push djangodemo DATABASE_URL --app vast-taiga-70981`

11) Connect db

    heroku pg:psql

12) Export db url

    export DATABASE_URL=postgres://$(whoami)

13) 
