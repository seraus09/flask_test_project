from flask import  Blueprint
from flask_restful import Resource, Api
import requests
from loguru import logger
from ipwhois import IPWhois
import json
import whois
from urllib.parse import urlparse
import re
from settings import *


api_bp = Blueprint('api_v1', __name__)
api_v1 = Api(api_bp)


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
        hostname = urlparse(host).hostname
        try:
            if re.match('http:|https:', host):
                if re.match(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', str(hostname)):
                    return IPWhois(hostname).lookup_whois(), 200
                else:
                    return json.dumps(whois.query(hostname).__dict__),200
            elif hostname is None:
                if re.match(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', str(host)):
                    return IPWhois(host).lookup_whois(), 200
                else:
                    result = whois.query(host).__dict__
                    return json.dumps(str(result)),200

            else:
                return {'error':'Not information about this zone'}, 400
        except Exception as error:
            logger.error(error)
            return {'error':'Not information about this zone'}, 400







api_v1.add_resource(GetGeo, '/api/geo/<string:host>')
api_v1.add_resource(WhoisInfo, '/api/whois/<string:host>')


