web: gunicorn task_scheduler.wsgi --log-file -
release: python manage.py makemigrations --noinput & python manage.py migrate --noinput
celery: celery -A task_scheduler worker -l info & celery -A task_scheduler beat -l info
