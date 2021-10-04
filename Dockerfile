FROM ubuntu:latest


ENV TZ="Europa/Kiev"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && apt-get install -y tzdata
RUN apt install -y  postgresql gcc python3-dev musl \
    openssl cargo g++ nodejs npm python3-setuptools python3-pip \
    whois vim

WORKDIR /var/www/site/app

COPY app /var/www/site/app


RUN pip3 install -r requirements.txt
