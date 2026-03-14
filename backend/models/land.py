from . import db
from datetime import datetime


class Land(db.Model):
    __tablename__ = 'lands'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmers.id', ondelete='CASCADE'), nullable=False)
    land_uid = db.Column(db.String(20), unique=True, nullable=False)
    village = db.Column(db.String(100), nullable=False)
    district = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    area_acres = db.Column(db.Numeric(10, 2), nullable=False)
    latitude = db.Column(db.Numeric(10, 7))
    longitude = db.Column(db.Numeric(10, 7))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    crop_mappings = db.relationship('LandCrop', backref='land', lazy=True, cascade='all, delete-orphan')

    @staticmethod
    def generate_land_uid():
        """Generate a unique land ID like LND-00001."""
        last_land = Land.query.order_by(Land.id.desc()).first()
        if last_land:
            num = last_land.id + 1
        else:
            num = 1
        return f"LND-{num:05d}"

    def to_dict(self):
        return {
            'id': self.id,
            'farmer_id': self.farmer_id,
            'land_uid': self.land_uid,
            'village': self.village,
            'district': self.district,
            'state': self.state,
            'area_acres': float(self.area_acres or 0),
            'latitude': float(self.latitude) if self.latitude else None,
            'longitude': float(self.longitude) if self.longitude else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'crop_mappings': [cm.to_dict() for cm in self.crop_mappings] if self.crop_mappings else []
        }
