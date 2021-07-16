from flask import Flask
from flask.signals import appcontext_popped
from flask_restful import  Api
from flask_cors import CORS
from api.views import api_bp
from api.settings import *


cors = CORS(resources={r"/api/*": {"origins": "*"}})

def create_app():
    app = Flask(__name__)
    
    cors.init_app(app)
    app.register_blueprint(api_bp)   
    return app

