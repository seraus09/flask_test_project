import socket
from flask import Blueprint, request
from flask_restful import Resource, Api, reqparse
import requests
from loguru import logger
from ipwhois import IPWhois
import whois
from urllib.parse import urlparse
from flask import current_app
import re


api_bp = Blueprint("api_v1", __name__)
api_v1 = Api(api_bp)

parser = reqparse.RequestParser()
parser.add_argument('host', dest='host')


class CleanHost():
    def __init__(self, host):
        self.host = host

    def get_clean_hostname(self):
        url = self.host
        if re.match("http:|https:|ftp:", str(url)):
            hostname = socket.getaddrinfo(urlparse(url).hostname, 443, proto=socket.IPPROTO_TCP)
            ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", str(hostname))
            clean_string = str(ip_candidates)[0:17].strip("[b''],'")
            logger.debug(clean_string)
            return str(clean_string.encode("idna")).lstrip("b").lstrip("'").rstrip("'")
        else:
            return str(url.encode("idna")).lstrip("b").rstrip("'").lstrip("'")


class GetGeo(Resource):
    def post(self):
        API_KEY = current_app.config["API_KEY"]
        host = request.get_json()['host']
        ip = CleanHost(host).get_clean_hostname()
        try:
            url = requests.get(f"http://api.ipstack.com/{ip}?access_key={API_KEY}")
            if url.status_code == 200:
                logger.debug(url.json())
                return url.json()
        except Exception as error:
            logger.error(error)


class WhoisInfo(Resource):
    def post(self):
        host = request.get_json()['host']
        hostname = urlparse(host).hostname
        whois_data = dict()
        time_data = dict()
        key_list = ["creation_date", "expiration_date", "last_updated", "name_servers"]
        try:
            if re.match("http:|https:", host):
                if re.match(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", str(hostname)):
                    return IPWhois(hostname).lookup_whois()['nets'][0], 200
                else:
                    for key_, value_ in whois.query(hostname).__dict__.items():
                        if key_ in key_list:
                            time_data[key_] = str(value_)
                        else:
                            whois_data[key_] = value_
                    return {"main_data": whois_data, "data": time_data}, 200
            elif hostname is None:
                if re.match(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", str(host)):
                    return IPWhois(host).lookup_whois()['nets'][0], 200
                else:
                    for key_, value_ in whois.query(host).__dict__.items():
                        if key_ in key_list:
                            time_data[key_] = str(value_)
                        else:
                            whois_data[key_] = value_
                    return {"main_data": whois_data, "data": time_data}, 200
            return {"error": "Not information about this zone"}, 400
        except Exception as error:
            logger.error(error)
        return {"error": "Not information about this zone "}, 400


api_v1.add_resource(GetGeo, "/api/geo/")
api_v1.add_resource(WhoisInfo, "/api/whois/")
