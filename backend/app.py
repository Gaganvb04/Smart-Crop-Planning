import os
import sys
from flask import Flask, send_from_directory
from flask_cors import CORS

# Add backend directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import DevelopmentConfig
from models import db
from routes import auth_bp, land_bp, crop_bp, analytics_bp, voice_bp
from utils.db_utils import init_db


def create_app(config_class=DevelopmentConfig):
    """Create and configure the Flask application."""
    app = Flask(__name__,
                static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'frontend'),
                static_url_path='')

    app.config.from_object(config_class)
    CORS(app, supports_credentials=True)

    # Initialize database
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(land_bp)
    app.register_blueprint(crop_bp)
    app.register_blueprint(analytics_bp)
    app.register_blueprint(voice_bp)

    # ---- Frontend Serving Routes ----

    @app.route('/')
    def serve_index():
        return send_from_directory(app.static_folder, 'index.html')

    @app.route('/pages/<path:filename>')
    def serve_pages(filename):
        return send_from_directory(os.path.join(app.static_folder, 'pages'), filename)

    @app.route('/css/<path:filename>')
    def serve_css(filename):
        return send_from_directory(os.path.join(app.static_folder, 'css'), filename)

    @app.route('/js/<path:filename>')
    def serve_js(filename):
        return send_from_directory(os.path.join(app.static_folder, 'js'), filename)

    @app.route('/assets/<path:filename>')
    def serve_assets(filename):
        return send_from_directory(os.path.join(app.static_folder, 'assets'), filename)

    return app


app = create_app()

# Create tables on first run
with app.app_context():
    db.create_all()
    from utils.db_utils import seed_crops_if_empty
    seed_crops_if_empty()

if __name__ == '__main__':
    print("Smart Crop Planning Server Starting...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, host='0.0.0.0', port=5000)
