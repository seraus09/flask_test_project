FROM tiangolo/uwsgi-nginx-flask:python3.6

WORKDIR /app
COPY app /app
RUN apt update && apt install whois
RUN pip3 install -r requirements.txt
