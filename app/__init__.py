from flask import Flask
from flask_cors import CORS
from config import Settings
from api.views import api_bp   



cors = CORS(resources={r"/api/*": {"origins": "*"}})

def create_app():
    
    app = Flask(__name__)
    app.config.from_object(Settings)

    cors.init_app(app)
    app.register_blueprint(api_bp) 
    
    return app

