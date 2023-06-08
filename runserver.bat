start msedge http://127.0.0.1:8000/
call venv\Scripts\activate
call docker run -p 6379:6379 -d redis:5
cd inf
python manage.py runserver 127.0.0.1:8000
