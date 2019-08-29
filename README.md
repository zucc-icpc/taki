# taki

It's the back-end of Programming Contest Lab Community project for ZUCC-ICPC-LAB.

See front-end project [here](https://github.com/zucc-icpc/mitsuha)

## Demo
[Here](http://47.100.57.37:8000)

## Install

This project uses [pipenv](https://github.com/pypa/pipenv) and Python3.7. Go check them out if you don't have them locally installed.

### Development environment

```
$ git clone https://github.com/zucc-icpc/taki.git
$ cd taki
Install all dependencies for a project
$ pipenv install
Spawns a shell within the virtualenv.
$ pipenv shell
Create tables to database which is specified in taki/taki/settings.py
$ python manage.py makemigrations
$ python manage.py migrate
Run server with hot load
$ python manage.py runserver
```

### Production environment
You need to modify taki/taki/settings.py, taki/taki_nginx.conf, and taki/taki_uwsig.ini to adapt your server first. 
see the [doc](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)

```
$ git clone https://github.com/zucc-icpc/taki.git
$ cd taki
Install all dependencies for a project
$ pipenv install
Spawns a shell within the virtualenv.
$ pipenv shell
Create tables to database which is specified in taki/taki/settings.py
$ python manage.py makemigrations
$ python manage.py migrate
Create and get into a screen (You can call the screen taki or anything you like)
$ screen -S taki
$ uwsgi --ini taki_uwsgi.ini
```
