import requests
import unittest




class ApiTest(unittest.TestCase):
    API_URL = 'http://127.0.0.1:5000'   
    
    def test_geo_endpoint(self):
       """ Test that the flask server is running and reachable"""
       r = requests.get(f'{ApiTest.API_URL}/api/geo/8.8.8.8')
       self.assertEqual(r.status_code, 200)
       self.assertEqual(r.json()['ip'],'8.8.8.8')
    
    def test_whois_domain(self):
        r = requests.get(f'{ApiTest.API_URL}/api/whois/google.com')
        self.assertEqual(r.status_code, 200)
    
    def test_whois_ip(self):
        r = requests.get(f'{ApiTest.API_URL}/api/whois/8.8.8.8')
        self.assertEqual(r.status_code, 200)
        
        

        
if __name__ == '__main__':
    unittest.main()


