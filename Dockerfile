FROM python:3.9-alpine
MAINTAINER NijatRajab

COPY ./requirements.txt /requirements.txt
COPY ./todo /todo
WORKDIR /todo

RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home django-njt
RUN apk del .tmp-build-deps

ENV PATH="/py/bin:$PATH"

USER django-njt

