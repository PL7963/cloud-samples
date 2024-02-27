FROM alpine:latest

RUN apk update
RUN apk add python3
RUN apk add py3-pip
RUN pip3 install functions-framework 

COPY ../cloud-function/main.py .

CMD ["functions-framework", "--target=main.py"]
