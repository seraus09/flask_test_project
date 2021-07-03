from flask import Flask
from flask_restful import Resource, Api
import requests
from loguru import logger
from flask_cors import CORS
from ipwhois import IPWhois
import json
from settings import *

app = Flask(__name__)
api=Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

class GetGeo(Resource):
    def get(self,host):
        try:
            url = requests.get(f'http://api.ipstack.com/{host}?access_key={API_KEY}')
            if url.status_code == 200:
                return url.json()
        except Exception as error:
            logger.error(error)

class WhoisInfo(Resource):
    def get(self,host):
        return IPWhois(host).lookup_whois()





api.add_resource(GetGeo, '/api/geo/<string:host>')
api.add_resource(WhoisInfo, '/api/whois/<string:host>')

if __name__ == '__main__':
    app.run(debug=True)
