from flask import Flask
from flask import render_template
import os
app = Flask(__name__)
@app.route('/')
@app.route('/index')

def index():
    cmd = "ping -c 4 8.8.8.8"
    res = os.popen(cmd).read()
    data = res.splitlines()
    return render_template('index.html', title = 'home', data = str('\n'.join(data)))

if __name__ == '__main__':
    app.run( debug=True, host='0.0.0.0' )