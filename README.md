## How to Dev

1. Clone repo
2. Create a virtualenv
3. Active virtualenv
4. Install dependences
5. Copy and edit your .env file
6. Install RabbitMQ

```console
git clone https://github.com/dssantos/task-scheduler-for-django.git task_scheduler
cd task_scheduler
python -m venv .task_scheduler
source .task_scheduler/bin/activate
pip install -r requirements-dev.txt
sudo apt install rabbitmq-server
cp contrib/env-sample .env
cat .env
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