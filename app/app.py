from flask import Flask, redirect, url_for, flash, request
from flask import render_template
from flask_bootstrap import Bootstrap
import requests, forms
from datetime import datetime
import os, json, ipaddress
from flask_moment import Moment

app = Flask(__name__)
Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = '808994589d35d4b4670642b1a3903548'
api_key = 'e811cf63b4083bb969ac6be16bea5d87'



class CheckHost():
    """Class for main page"""
    def __init__(self, host):
        self.host = host


    def geoIP(self):
        """Get results for api """
        ip = (self.host)
        url = requests.get(f'http://api.ipstack.com/{ip}?access_key={api_key}') #get api request
        if url.status_code == 200:
            return url.json()

    def get_hostname(self):
        """The method  for find out hostname"""
        get_ip = (self.host)
        cmd = (f"nslookup {get_ip} | head -n 1 | cut -d'=' -f2") #getting hostname
        hostname = os.popen(cmd).read()
        if "can't" in hostname:
            return get_ip
        else:
            return hostname

@app.route('/' , methods=['GET', 'POST'])
def index():
    """Index page"""
    try:
        ip = None
        form = forms.TypeIP()
        if form.validate_on_submit() and request.method == 'POST':
            ip = CheckHost(form.ip.data)
            data = ip.geoIP()
            check = data.get('type')
            addr = data.get("ip")
            if ipaddress.ip_address(addr).is_loopback or check == None:
                flash(f'No info found for host {addr}, maybe localhost or private network?')
                return render_template('index.html', form=form, current_time=datetime.utcnow(), real_ip=request.remote_addr)
            country = data.get("country_name")
            region = data.get("region_name")
            city = data.get("city")
            real_ip = request.remote_addr
            flag = data.get('location').get('country_flag_emoji')
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            hostname = CheckHost(addr).get_hostname()


        else:
            return  render_template('index.html', form=form, current_time=datetime.utcnow(), real_ip=request.remote_addr)


        return render_template('test.html', flag=flag, data=data, current_time=datetime.utcnow(), real_ip=real_ip,
                               form=form, hostname=hostname, ip=ip, addr=addr,country=country, region=region,
                               city=city, latitude=latitude, longitude=longitude)

    except Exception as error:
        flash(f'Ooops... Something went wrong !!! {error}')
        return render_template('index.html', form=form, current_time=datetime.utcnow(), real_ip=request.remote_addr)


if __name__ ==  '__main__':
    app.run(debug=True, host='0.0.0.0')
