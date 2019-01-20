web: gunicorn config.wsgi:application
worker: celery worker --app=learn_islam.taskapp --loglevel=info
