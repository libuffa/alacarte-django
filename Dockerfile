FROM python:3.7-alpine
MAINTAINER Lautaro Buffa

ENV PYTHONUNUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# setea la app aca
RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
