FROM python:3

RUN pip install django==5.1.3

COPY . .

RUN django-admin startproject myproject .
EXPOSE 8000
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]