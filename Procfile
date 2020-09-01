release: python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn todolist.wsgi --log-file -
