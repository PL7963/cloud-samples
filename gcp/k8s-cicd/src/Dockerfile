FROM alpine:latest
RUN apk add python3
RUN apk add py3-pip
RUN pip3 install flask --break-system-packages

COPY . /app

CMD ["python3", "app/main.py"]

EXPOSE 80
