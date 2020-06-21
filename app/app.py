from flask import Flask, redirect, url_for, flash, request
from flask import render_template
from flask_bootstrap import Bootstrap
import requests
import forms
from datetime import datetime
import os, json
from flask_moment import Moment

app = Flask(__name__)
Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = 'hard to guess string'
api_key = 'e811cf63b4083bb969ac6be16bea5d87'

class CheckHost():

    def __init__(self, host):
        self.host = host


    def geoIP(self):
        ip = (self.host)
        url = requests.get(f'http://api.ipstack.com/{ip}?access_key={api_key}')
        if url.status_code == 200:
            return url.json()
        else:
            return "Error"

    def get_hostname(self):
        get_ip = (self.host)
        cmd = (f"nslookup {get_ip} | head -n 1 | cut -d'=' -f2")
        hostname = os.popen(cmd).read()
        return hostname



@app.route('/' , methods=['GET', 'POST'])
def index():
    ip = None
    form = forms.TypeIP()
    if form.validate_on_submit() and request.method == 'POST':
        ip = CheckHost(form.ip.data)
        data = ip.geoIP()
        addr = data.get("ip")
        country = data.get("country_name")
        region = data.get("region_name")
        city = data.get("city")
        real_ip = request.remote_addr
        flag = data.get('location').get('country_flag_emoji')
        hostname = ip.get_hostname()
    else:
        return  render_template('index.html', form=form, current_time=datetime.utcnow(),real_ip=request.remote_addr)

    return render_template('main.html',flag=flag, current_time=datetime.utcnow(),real_ip=real_ip,
                           form=form,hostname=hostname,ip=ip, addr=addr, country=country, region=region, city=city)


if __name__ ==  '__main__':
    app.run(debug=True, host='0.0.0.0')
