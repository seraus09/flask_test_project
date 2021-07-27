import socket
from flask import  Blueprint
from flask_restful import Resource, Api
import requests
from loguru import logger
from ipwhois import IPWhois
import json
import whois
from urllib.parse import urlparse
from flask import current_app
import re



api_bp = Blueprint('api_v1', __name__)
api_v1 = Api(api_bp)

class CleanHost():
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



class GetGeo(Resource):
    def get(self,host):
        API_KEY = current_app.config["API_KEY"]
        ip =  CleanHost(host).get_clean_hostname()
        try:
            url = requests.get(f'http://api.ipstack.com/{ip}?access_key={API_KEY}')
            if url.status_code == 200:
                logger.debug(url.json())
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



