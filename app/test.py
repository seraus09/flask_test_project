import os
import requests

def geoIP(ip):
    url = requests.get(f'http://api.ipstack.com/{ip}?access_key=e811cf63b4083bb969ac6be16bea5d87')
    if url.status_code == 200:
        return url.text
    else:
        return "Error"
ip = "zomro.com"
print(geoIP(ip))