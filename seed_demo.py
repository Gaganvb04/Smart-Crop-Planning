"""Seed demo farmer and lands into the database."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from app import app, db
from models import Farmer, Land

with app.app_context():
    # Check if demo farmer exists
    farmer = Farmer.query.filter_by(mobile='9999999999').first()

    if not farmer:
        farmer = Farmer(
            name='Rajesh Kumar',
            mobile='9999999999',
            preferred_language='en',
            total_land_acres=8.5
        )
        farmer.set_password('1234')
        db.session.add(farmer)
        db.session.flush()
        print("Created demo farmer (mobile: 9999999999, password: 1234)")

    land_count = Land.query.filter_by(farmer_id=farmer.id).count()
    if land_count > 0:
        print(f"Farmer already has {land_count} lands")
        sys.exit(0)

    lands = [
        Land(farmer_id=farmer.id, land_uid='LND-D0001',
             village='Rampur', district='Varanasi', state='Uttar Pradesh',
             area_acres=2.0, latitude=25.3176, longitude=82.9739),
        Land(farmer_id=farmer.id, land_uid='LND-D0002',
             village='Shivpur', district='Varanasi', state='Uttar Pradesh',
             area_acres=1.5, latitude=25.2854, longitude=82.9916),
        Land(farmer_id=farmer.id, land_uid='LND-D0003',
             village='Kotwa', district='Chandauli', state='Uttar Pradesh',
             area_acres=1.5, latitude=25.2584, longitude=83.2632),
        Land(farmer_id=farmer.id, land_uid='LND-D0004',
             village='Hubli', district='Dharwad', state='Karnataka',
             area_acres=2.0, latitude=15.3647, longitude=75.1240),
        Land(farmer_id=farmer.id, land_uid='LND-D0005',
             village='Gadag', district='Gadag', state='Karnataka',
             area_acres=1.5, latitude=15.4315, longitude=75.6355),
    ]
    db.session.add_all(lands)
    db.session.commit()
    print(f"Added {len(lands)} lands for farmer {farmer.name}")
    print("Login: mobile=9999999999, password=1234")
