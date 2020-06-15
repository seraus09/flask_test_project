from flask import Flask, redirect
from flask import render_template
from flask_bootstrap import Bootstrap
import requests
import forms
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
Bootstrap(app)

def ping(ip):
    cmd = f"ping -c 4 {ip}"
    res = os.popen(cmd).read()
    data = res.splitlines()
    results = (data[0],data[7],data[8])
    return results

@app.route('/' , methods=['GET', 'POST'])
def index():
    ip = None
    form = forms.TypeIP()
    if form.validate_on_submit():
        ip = form.ip.data
    return render_template('index.html', form=form, ip=ip), data=ping(ip))



if __name__ == '__main__':
    app.run( debug=True, host='0.0.0.0' )