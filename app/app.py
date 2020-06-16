from flask import Flask, redirect
from flask import render_template
from flask_bootstrap import Bootstrap
import requests
import forms
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
Bootstrap(app)

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
    return render_template('index.html', form=form, ip=ip, data=data )



if __name__ == '__main__':
    app.run( debug=True, host='0.0.0.0' )
