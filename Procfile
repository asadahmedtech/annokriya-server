web: gunicorn backend.wsgi --log-file - 
web: python manage.py runserver 0.0.0.0:$PORT --noreload
heroku config:set DISABLE_COLLECTSTATIC=1
