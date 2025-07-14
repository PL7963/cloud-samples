FROM python:latest

COPY . /app

RUN pip install flask pymysql gunicorn

WORKDIR /app

CMD gunicorn -b 0.0.0.0:8080 main:app

EXPOSE 8080
