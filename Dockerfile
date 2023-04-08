FROM tiangolo/uwsgi-nginx-flask:python3.11

ENV STATIC_PATH /app/static
ENV STATIC_URL /static

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app