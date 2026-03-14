from . import db
from datetime import datetime


class LandCrop(db.Model):
    __tablename__ = 'land_crops'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    land_id = db.Column(db.Integer, db.ForeignKey('lands.id', ondelete='CASCADE'), nullable=False)
    crop_id = db.Column(db.Integer, db.ForeignKey('crops.id', ondelete='CASCADE'), nullable=False)
    season = db.Column(db.Enum('Kharif', 'Rabi', 'Zaid'), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Unique constraint: one crop per land per season per year
    __table_args__ = (
        db.UniqueConstraint('land_id', 'season', 'year', name='unique_land_season_year'),
    )

    def to_dict(self):
        return {
            'id': self.id,
            'land_id': self.land_id,
            'crop_id': self.crop_id,
            'crop_name': self.crop.name if self.crop else None,
            'crop_icon': self.crop.icon if self.crop else '🌾',
            'season': self.season,
            'year': self.year
        }
