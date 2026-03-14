from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .farmer import Farmer
from .land import Land
from .crop import Crop
from .land_crop import LandCrop

__all__ = ['db', 'Farmer', 'Land', 'Crop', 'LandCrop']
