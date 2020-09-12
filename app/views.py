from flask import Flask, redirect, url_for, flash, request
from flask import render_template
from flask_bootstrap import Bootstrap
import requests, forms
from datetime import datetime
import os, json, ipaddress
from flask_moment import Moment
import concurrent.futures
import socket
from urllib.parse import urlparse
import re


app = Flask(__name__)
Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = '808994589d35d4b4670642b1a3903548'
api_key = 'e811cf63b4083bb969ac6be16bea5d87'




class CheckHost():
    """Class for getting different result"""
    def __init__(self, host):
        self.host = host

    def get_clean_hostname(self):
        url = self.host
        if re.match('http:|https:|ftp:', str(url)):
            hostname = socket.getaddrinfo(urlparse(url).hostname, 443, proto=socket.IPPROTO_TCP)
            ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", str(hostname))
            clean_string = str(ip_candidates)[0:17].rstrip(']').rstrip("'").lstrip("[").lstrip("'").rstrip(",").rstrip("'")
            return clean_string
        else:
            return url

    def get_result_from_api_ipstack(self):
        ip = CheckHost.get_clean_hostname(self)
        url = requests.get(f'http://api.ipstack.com/{ip}?access_key={api_key}') #get api request
        if url.status_code == 200:
            return url.json()

    def get_hostname(self):
        try:
            get_ip = (self.host)
            hostname = socket.gethostbyaddr(get_ip)
            return hostname[0]
        except:
            return get_ip


    def get_ping(self):
        get_host = CheckHost.get_clean_hostname(self)
        url = requests.get(f'http://91.201.25.57/api/v1.0/tasks/{get_host}', auth=('sera', '12345'))
        if url.status_code == 200:
            return url.json()

class MainPage():
     """Show information on page"""



     def get_information_from_form():
         form = forms.TypeIP()
         host = form.field_data.data
         ip = CheckHost(host)
         ip_information = ip.get_result_from_api_ipstack()
         return ip_information

     def return_ping_page():
         """Return information from the 'ping' button"""
         form = forms.TypeIP()
         ip = CheckHost(form.field_data.data)
         data = CheckHost.get_ping(ip)
         packet = data.get('packet')
         return render_template('test.html', form=form,current_time=datetime.utcnow(),
                                local=int(packet), virt=int(packet),real_ip=request.remote_addr)


     def return_index_page_if_error():
        return render_template('index.html', form=forms.TypeIP(),
                               current_time=datetime.utcnow(), real_ip=request.remote_addr)

     def return_check_page():
        """Return information from the 'check' button"""
        form = forms.TypeIP()
        ip_information = MainPage.get_information_from_form()
        return render_template('main.html', flag=ip_information.get('location').get('country_flag_emoji'),
                               data=ip_information, current_time=datetime.utcnow(), real_ip=request.remote_addr,
                               form=form, hostname=CheckHost(ip_information.get("ip")).get_hostname(),
                               addr=ip_information.get("ip"),
                               country=ip_information.get("country_name"), region=ip_information.get("region_name"),
                               city=ip_information.get("city"), latitude=ip_information.get('latitude'),
                               longitude=ip_information.get('longitude'))


@app.route('/', methods=['GET', 'POST'])
def return_index_page():
    try:

        form = forms.TypeIP()
        if form.validate_on_submit() == form.submit.data and request.method == 'POST':
            if MainPage.get_information_from_form().get('type') is None:
                flash(f"No info found for host {MainPage.get_information_from_form().get('ip')}, maybe localhost or private network?")
                return MainPage.return_index_page_if_error()
            else:
                return MainPage.return_check_page()

        elif form.validate_on_submit() == form.ping.data and request.method == 'POST':
            return MainPage.return_ping_page()

        else:
            return  MainPage.return_index_page_if_error()

    except Exception as error:
        flash(f'Ooops... Something went wrong !!! {error}')
        return MainPage.return_index_page_if_error()



if __name__ ==  '__main__':
    app.run(debug=True, host='0.0.0.0')
