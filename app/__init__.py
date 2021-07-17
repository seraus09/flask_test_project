from flask import Flask
from flask_cors import CORS
from api.views import api_bp
from config import Settings



cors = CORS(resources={r"/api/*": {"origins": "*"}})

def create_app():
    app = Flask(__name__)
    
    cors.init_app(app)
    app.config.from_object(Settings)   
    app.register_blueprint(api_bp) 
    return app

