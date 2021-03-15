FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

RUN groupadd user && useradd --create-home --home-dir /home/user -g user user
WORKDIR /var/www/app

RUN apt-get update && apt-get install gcc build-essential libpq-dev -y && \
    python3 -m pip install --no-cache-dir pip-tools

COPY ./requirements.txt /var/www/app

RUN pip install -r requirements.txt

RUN apt-get purge libpq-dev -y && apt-get autoremove -y && \
    rm /var/lib/apt/lists/* rm -rf /var/cache/apt/*

COPY . /var/www/app

USER user

CMD ["sh","-c", \
    " python manage.py test && \
     gunicorn coolfreela.wsgi --log-file - -b 0.0.0.0:8000 --reload"]


