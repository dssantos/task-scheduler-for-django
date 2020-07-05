## How to Dev

1. Clone repo
2. Create a virtualenv
3. Active virtualenv
4. Install dependences
5. Edit SECRET_KEY in .env file

```console
git clone https://github.com/dssantos/task-scheduler-for-django.git task_scheduler
cd task_scheduler
python -m venv .task_scheduler
source .task_scheduler/bin/activate
pip install --upgrade pip
pip install -r requirements-dev.txt
cp contrib/env-sample .env
cat .env
```

## How to Deploy in Heroku

1. Login in Heroku
2. Edit Procfile
3. Git Add and Commit
4. Create Heroku App
5. Set environments variables
6. Push to Heroku
7. Active Celery Dyno
8. Create Django user
9. Open App on Browser

```console
heroku login
echo -e """\
web: gunicorn task_scheduler.wsgi --log-file -
release: python manage.py makemigrations --noinput $ python manage.py migrate --noinput
celery: celery -A task_scheduler worker -l info & celery -A task_scheduler beat -l info
""" > Procfile
git add .
git commit -m 'Deploy in Heroku'
heroku apps:create
heroku config:set SECRET_KEY='XXXXXXXXXXXXXXXXXXXXXX'
heroku config:set DEBUG=True
git push heroku master --force
heroku ps:scale celery=1
python manage.py createsuperuser
heroku open
```

## How to Use

1. Make migrations
2. Run migrations
3. Create Django user

```console
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

4. Run this three commands in differents terminals

```console
python manage.py runserver
celery -A task_scheduler worker -l info
celery -A task_scheduler beat -l info
```

5. Browse to http://127.0.0.1:8000/admin
6. Configure schedules in [Periodic tasks](http://127.0.0.1:8000/admin/django_celery_beat/periodictask/) and set the arguments
7. Check results in [Numero](http://127.0.0.1:8000/admin/core/numero/)