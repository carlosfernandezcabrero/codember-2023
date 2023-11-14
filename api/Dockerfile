FROM python:3.12-alpine3.18 as builder

WORKDIR /python-docker

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt \
    && pip install waitress

COPY . .

CMD waitress-serve --port 5000 --host 0.0.0.0 --call "app:create_app"