FROM python:3.6

RUN pip3 install Flask==0.10.1 requests==2.5.1  requests==2.5.1 redis==2.10.3 Flask-Bootstrap==3.3.7 Flask-WTF==2.3.1

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
WORKDIR /app
COPY app /app
EXPOSE 9090 9191
USER uwsgi
