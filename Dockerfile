FROM python:3-alpine
MAINTAINER NijatRajab

COPY ./requirements.txt /requirements.txt
COPY ./todo /todo
WORKDIR /todo

RUN apk add --update --no-cache postgresql-client libpq
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers build-base postgresql-dev python3-dev musl-dev zlib zlib-dev postgresql-libs
RUN python -m venv /py && \
    /py/bin/pip3 install --upgrade pip && \
    /py/bin/pip3 install -r /requirements.txt && \
    adduser --disabled-password --no-create-home django-njt
RUN apk del .tmp-build-deps

ENV PATH="/py/bin:$PATH"

USER django-njt
