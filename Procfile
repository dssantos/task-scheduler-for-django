web: gunicorn task_scheduler.wsgi --log-file - & celery -A task_scheduler worker -l info & celery -A task_scheduler beat -l info & wait -n
release: python manage.py migrate --noinput
