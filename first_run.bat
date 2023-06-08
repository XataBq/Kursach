call python -m venv venv
call venv\Scripts\activate
pip install Django Pillow django-ckeditor random2 redis
pip install -U channels["daphne"] channels_redis
rem cd inf
rem python manage.py runserver 127.0.0.1:8000
rem start msedge http://127.0.0.1:8000/
pause