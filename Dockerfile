FROM python:3.6

RUN pip3 install Flask==0.10.1 requests==2.5.1 Flask-Bootstrap==3.3.7 Flask-WTF flask-moment fabric
RUN apt update && apt install dnsutils -y
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
WORKDIR /app
COPY /app /app
COPY cmd.sh /
RUN chmod +x /cmd.sh
EXPOSE 5000 5000
USER uwsgi
CMD ["/cmd.sh"]
