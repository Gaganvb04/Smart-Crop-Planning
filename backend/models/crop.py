from . import db
from datetime import datetime


class Crop(db.Model):
    __tablename__ = 'crops'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    season = db.Column(db.Enum('Kharif', 'Rabi', 'Zaid'), nullable=False)
    sowing_period = db.Column(db.String(100))
    icon = db.Column(db.String(50), default='🌾')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    land_mappings = db.relationship('LandCrop', backref='crop', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'season': self.season,
            'sowing_period': self.sowing_period,
            'icon': self.icon
        }
