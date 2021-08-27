from flask import Flask
from flask_cors import CORS
from config import Settings
from api.views import api_bp   
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


cors = CORS(resources={r"/api/*": {"origins": "*"}})

def create_app():
    
    sentry_sdk.init(
        dsn="https://5e342ea2686441a8b7bfa37ca07e5cc4@o977854.ingest.sentry.io/5934189",
        integrations=[FlaskIntegration()],
        traces_sample_rate=1.0)

    app = Flask(__name__)
    app.config.from_object(Settings)

    cors.init_app(app)
    app.register_blueprint(api_bp) 
    
    return app

