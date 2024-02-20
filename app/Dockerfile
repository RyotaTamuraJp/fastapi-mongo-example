FROM python:3.11.1-slim-bullseye

WORKDIR /app

COPY ./ ./

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install wget -y \
  && pip install -U pip \
  && pip install poetry \
  && poetry run pip install -U pip setuptools \
  && poetry install \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV PYTHONPATH=/app
ENV LANG ja_JP.UTF-8

CMD [ "./start.sh" ]
