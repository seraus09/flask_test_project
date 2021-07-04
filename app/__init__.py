from flask import Flask
from flask_restful import  Api
from flask_cors import CORS


api=Api()
cors = CORS(resources={r"/api/*": {"origins": "*"}})

def create_app():
    app = Flask(__name__)
    api.init_app(app)
    cors.init_app(app)   
    return app

