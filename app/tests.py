import json
import unittest

from __init__ import create_app
from flask_testing import TestCase


class BaseTestCase(TestCase):
    def create_app(self):
        app = create_app()
        return app


class ApiTest(BaseTestCase):

    def test_geo_endpoint(self):
        response = self.client.post("/api/geo/", json={"host": "8.8.8.8"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["ip"], "8.8.8.8")

    def test_whois_endpoint(self):
        response = self.client.post("/api/whois/", json={"host": "yandex.ru"})
        self.assertEqual(response.status_code, 200)

    def test_api_with_shema(self):
        response = self.client.post("/api/whois/", json={"host": "https://yandex.ru"})
        self.assertEqual(response.status_code, 200)

    def test_whois_fail(self):
        response = self.client.post("/api/whois/", json={"host": "ttt.cf"})
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
