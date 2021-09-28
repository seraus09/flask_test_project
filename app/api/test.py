import requests
h = 'http://127.0.0.1:5000/api/geo/'
data = {'host':'zomro.com'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(h, json=data, headers=headers)
print(r.text)
