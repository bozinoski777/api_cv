release: python manage.py makemigrations
release: python manage.py migrate

web: gunicorn api_cv.wsgi
