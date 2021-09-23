release: python manage.py migrate
web: gunicorn CCMS.wsgi --log-file -
heroku logs --tail
