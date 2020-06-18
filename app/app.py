from flask import Flask, redirect, url_for, flash, request
from flask import render_template
from flask_bootstrap import Bootstrap
import requests
import forms
from datetime import datetime
import os
from flask_moment import Moment


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
Bootstrap(app)
moment = Moment(app)

class MainPage():

    def __init__(self, ipaddr):
        self.ipaddr = ipaddr

    def geoIP(self):
        ip = (self.ipaddr)
        url = requests.get(f'http://api.db-ip.com/v2/free/{ip}')
        if url.status_code == 200:
            return url.text
        else:
            return "Error"

@app.route('/' , methods=['GET', 'POST'])
def index():
    ip = None
    form = forms.TypeIP()
    if form.validate_on_submit():
        ip = MainPage(form.ip.data)
        data = ip.geoIP()
        res = dict(eval(data))
        addr = res.get("ipAddress")
        country = res.get("continentName")
        region = res.get("stateProv")
        city = res.get("city")
        real_ip = request.remote_addr
    else:
        return  render_template('index.html', form=form, current_time=datetime.utcnow(),real_ip=request.remote_addr)

    return render_template('main.html', current_time=datetime.utcnow(),real_ip=real_ip, form=form, ip=ip, addr=addr, country=country, region=region, city=city)



if __name__ == '__main__':
    app.run( debug=True, host='0.0.0.0' )
