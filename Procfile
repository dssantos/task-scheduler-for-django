web: gunicorn task_scheduler.wsgi --log-file -
release: python manage.py migrate --noinput
worker: celery -A task_scheduler worker -l info & celery -A task_scheduler beat -l info
