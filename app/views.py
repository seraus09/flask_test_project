from flask import Flask, flash, request
from flask import render_template
from flask_bootstrap import Bootstrap
import requests, forms
from datetime import datetime
from flask_moment import Moment
import concurrent.futures
import socket
from urllib.parse import urlparse
import re
from ipwhois import IPWhois
import whois
from settings import *



app = Flask(__name__)
app.config.from_pyfile('settings.py')
Bootstrap(app)
moment = Moment(app)


class CheckHost():
    """Class for getting different result"""
    def __init__(self, host):
        self.host = host

    def get_clean_hostname(self):
        url = self.host
        if re.match('http:|https:|ftp:', str(url)):
            hostname = socket.getaddrinfo(urlparse(url).hostname, 443, proto=socket.IPPROTO_TCP)
            ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", str(hostname))
            clean_string = str(ip_candidates)[0:17].rstrip(']').rstrip("'").lstrip("[").lstrip("'").lstrip("b").rstrip(",").rstrip("'")
            return str(clean_string.encode('idna')).lstrip('b').lstrip("'").rstrip("'")
        else:
            return str(url.encode('idna')).lstrip('b').rstrip("'").lstrip("'")

    def get_result_from_api_ipstack(self):
        ip = CheckHost.get_clean_hostname(self)
        url = requests.get(f'http://api.ipstack.com/{ip}?access_key={API_KEY}') #get api request
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
        thread = concurrent.futures.ThreadPoolExecutor()
        get_host = CheckHost.get_clean_hostname(self)
        nodes = ['185.250.206.220']
        result = []
        try:
            url = lambda node: requests.get(f'http://{node}/api/v1.0/tasks/{get_host}', auth=('sera', '12345'))
            for packet in thread.map(url,nodes):
                if packet.status_code == 200:
                    result.append(packet.json().get('packet'))
            return result
        finally:
            result.append(0)
            return result
    


class MainPage():
     """Show information on page"""

     def return_captcha():
         count_ip = REDIS_CONNECT.incrby(request.remote_addr, 1)
         max_requests = 6
         if count_ip >= max_requests:
             return forms.Recaptacha()
     

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
         return render_template('ping.html', form=form,current_time=datetime.utcnow(),
                                local=int(data[0]), virt=int(0),aws=int(0),real_ip=request.remote_addr, data=MainPage.return_captcha())


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


     def return_whois_page():
         form = forms.TypeIP()
         host = form.field_data.data
         domain = urlparse(host).hostname
         try:
             if re.match('http:|https:', host):
                 if re.match(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", str(domain)):
                     return render_template('ipwhois.html', form=forms.TypeIP(),
                                            current_time=datetime.utcnow(), real_ip=request.remote_addr,
                                            data=IPWhois(domain).lookup_whois(),
                                            address=IPWhois(domain).lookup_whois().get('nets')[0].get('address'),
                                            cidr=IPWhois(domain).lookup_whois().get('nets')[0].get('cidr'),
                                            city=IPWhois(domain).lookup_whois().get('nets')[0].get('city'),
                                            country=IPWhois(domain).lookup_whois().get('nets')[0].get('country'),
                                            created=IPWhois(domain).lookup_whois().get('nets')[0].get('created'),
                                            description=IPWhois(domain).lookup_whois().get('nets')[0].get('description'),
                                            emails=IPWhois(domain).lookup_whois().get('nets')[0].get('emails'),
                                            handle=IPWhois(domain).lookup_whois().get('nets')[0].get('handle'),
                                            name=IPWhois(domain).lookup_whois().get('nets')[0].get('name'),
                                            postal_code=IPWhois(domain).lookup_whois().get('nets')[0].get('postal_code'),
                                            range=IPWhois(domain).lookup_whois().get('nets')[0].get('range'),
                                            state=IPWhois(domain).lookup_whois().get('nets')[0].get('state'),
                                            updated=IPWhois(domain).lookup_whois().get('nets')[0].get('updated'), )
                 else:
                     return render_template('whois.html', form=forms.TypeIP(),
                                            current_time=datetime.utcnow(), real_ip=request.remote_addr,
                                            data=whois.query(domain).__dict__,
                                            name=whois.query(domain).__dict__.get('name'),
                                            reg=whois.query(domain).__dict__.get('registrar'),
                                            create=whois.query(domain).__dict__.get('creation_date'),
                                            expiration=whois.query(domain).__dict__.get('expiration_date'),
                                            updated=whois.query(domain).__dict__.get('last_updated'),
                                            status=whois.query(domain).__dict__.get('status'),
                                            ns=whois.query(domain).__dict__.get('name_servers'))
             elif domain is None:
                 if re.match(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", str(host)):
                     return render_template('ipwhois.html', form=forms.TypeIP(),
                                            current_time=datetime.utcnow(), real_ip=request.remote_addr,
                                            data=IPWhois(host).lookup_whois(),address=IPWhois(host).lookup_whois().get('nets')[0].get('address'),
                                            cidr=IPWhois(host).lookup_whois().get('nets')[0].get('cidr'),
                                            city=IPWhois(host).lookup_whois().get('nets')[0].get('city'),
                                            country=IPWhois(host).lookup_whois().get('nets')[0].get('country'),
                                            created=IPWhois(host).lookup_whois().get('nets')[0].get('created'),
                                            description=IPWhois(host).lookup_whois().get('nets')[0].get('description'),
                                            emails=IPWhois(host).lookup_whois().get('nets')[0].get('emails'),
                                            handle=IPWhois(host).lookup_whois().get('nets')[0].get('handle'),
                                            name=IPWhois(host).lookup_whois().get('nets')[0].get('name'),
                                            postal_code=IPWhois(host).lookup_whois().get('nets')[0].get('postal_code'),
                                            range=IPWhois(host).lookup_whois().get('nets')[0].get('range'),
                                            state=IPWhois(host).lookup_whois().get('nets')[0].get('state'),
                                            updated=IPWhois(host).lookup_whois().get('nets')[0].get('updated'),)
                 else:
                     return render_template('whois.html', form=forms.TypeIP(),
                                            current_time=datetime.utcnow(), real_ip=request.remote_addr,
                                            data=whois.query(host).__dict__,
                                            name=whois.query(host).__dict__.get('name'),
                                            reg=whois.query(host).__dict__.get('registrar'),
                                            create=whois.query(host).__dict__.get('creation_date'),
                                            expiration=whois.query(host).__dict__.get('expiration_date'),
                                            updated=whois.query(host).__dict__.get('last_updated'),
                                            status=whois.query(host).__dict__.get('status'),
                                            ns=whois.query(host).__dict__.get('name_servers'))
             else:
                 flash(f"Not information about this zone")
                 return MainPage.return_index_page_if_error()

         except Exception as err:
             flash(f"Not information about this zone{err}")
             return MainPage.return_index_page_if_error()

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


        elif form.validate_on_submit() == form.whois.data and request.method == 'POST':
            return MainPage.return_whois_page()

        else:
            return  MainPage.return_index_page_if_error()

    except Exception as error:
        flash(f'Ooops... Something went wrong !!! {error}')

        return MainPage.return_index_page_if_error()
        


@app.route('/getdata/<index_no>', methods=['POST'])
def data_get(index_no):
    """Data fetch from js function"""
    if request.method == 'POST': # POST request
        len_key  = len(index_no)
        if len_key == 484:
            REDIS_CONNECT.getset(request.remote_addr, 0)
    

if __name__ ==  '__main__':
    app.run(debug=True, host='0.0.0.0')


