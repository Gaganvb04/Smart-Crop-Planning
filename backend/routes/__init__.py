# Routes package
from .auth_routes import auth_bp
from .land_routes import land_bp
from .crop_routes import crop_bp
from .analytics_routes import analytics_bp
from .voice_routes import voice_bp

__all__ = ['auth_bp', 'land_bp', 'crop_bp', 'analytics_bp', 'voice_bp']
