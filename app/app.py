from flask import Flask, redirect, url_for, flash, request
from flask import render_template
from flask_bootstrap import Bootstrap
import requests, forms
from datetime import datetime
import os, json, ipaddress
from flask_moment import Moment
from flask import jsonify
from fabric import Connection
import concurrent.futures

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

    def get_ping(self):
        """'The method for check ping"""
        get_host = (self.host)
        thread = concurrent.futures.ThreadPoolExecutor()
        # command = os.popen(f"ping -c4 {get_host } | tail  -2 | head -1 ").read().split(" ").pop(3)
        server_list = ['91.201.25.57', '185.250.206.220','35.178.203.123']
        awk = "awk '{print $1}'"
        cmd = f'''ping -c 4 {get_host} | tail  -2 | head -1 | cut -d "," -f 2 | {awk} '''
        fun = lambda x: Connection(f'root@{x}').run(cmd, hide=True).stdout
        g = []
        for i in thread.map(fun, server_list):
            g.append(str(i).rstrip('\n'))
        return g


@app.route('/' , methods=['GET', 'POST'])
def index():
    """Index page"""
    try:
        ip = None
        form = forms.TypeIP()
        check_button = form.submit.data
        ping_button = form.ping.data
        if form.validate_on_submit() == check_button and request.method == 'POST':
            ip = CheckHost(form.ip.data)
            data = ip.geoIP()
            check = data.get('type')
            addr = data.get("ip")
            if check == None:
                flash(f'No info found for host {addr}, maybe localhost or private network?')
                return render_template('index.html', form=form,
                                       current_time=datetime.utcnow(), real_ip=request.remote_addr)

        elif form.validate_on_submit() == ping_button and request.method == 'POST':
            ip = CheckHost(form.ip.data)
            data = CheckHost.get_ping(ip)
            return render_template('test.html', form=form,
                                   current_time=datetime.utcnow(), local=int(data[0]), virt=int(data[1]),amazon=int(data[2]),
                                   real_ip=request.remote_addr)


        else:
            return  render_template('index.html', form=form,
                                    current_time=datetime.utcnow(), real_ip=request.remote_addr)

        return render_template('main.html', flag = data.get('location').get('country_flag_emoji'),
                               data = data, current_time = datetime.utcnow(), real_ip = request.remote_addr,
                               form = form, hostname = CheckHost(addr).get_hostname(), ip = ip, addr = addr,
                               country = data.get("country_name"),region = data.get("region_name"),
                               city = data.get("city"), latitude = data.get('latitude'), longitude = data.get('longitude'))
    except Exception as error:
        flash(f'Ooops... Something went wrong !!! {error}')
        return render_template('index.html', form=form, current_time=datetime.utcnow(), real_ip=request.remote_addr)





if __name__ ==  '__main__':
    app.run(debug=True, host='0.0.0.0')
