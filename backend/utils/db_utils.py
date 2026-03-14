from models import db, Crop, Farmer, Land


def init_db(app):
    """Initialize the database and create tables."""
    with app.app_context():
        db.create_all()
        seed_crops_if_empty()


def seed_crops_if_empty():
    """Seed crop master data if the table is empty."""
    if Crop.query.count() > 0:
        return

    crops = [
        # Kharif
        Crop(name='Rice', season='Kharif', sowing_period='June - July', icon='🌾'),
        Crop(name='Maize', season='Kharif', sowing_period='June - July', icon='🌽'),
        Crop(name='Cotton', season='Kharif', sowing_period='April - May', icon='☁️'),
        Crop(name='Sugarcane', season='Kharif', sowing_period='February - March', icon='🎋'),
        Crop(name='Groundnut', season='Kharif', sowing_period='June - July', icon='🥜'),
        Crop(name='Soybean', season='Kharif', sowing_period='June - July', icon='🫘'),
        Crop(name='Jowar (Sorghum)', season='Kharif', sowing_period='June - July', icon='🌾'),
        Crop(name='Bajra (Pearl Millet)', season='Kharif', sowing_period='June - July', icon='🌾'),
        Crop(name='Tur (Pigeon Pea)', season='Kharif', sowing_period='June - July', icon='🌱'),
        Crop(name='Ragi (Finger Millet)', season='Kharif', sowing_period='June - July', icon='🌾'),
        # Rabi
        Crop(name='Wheat', season='Rabi', sowing_period='October - November', icon='🌾'),
        Crop(name='Barley', season='Rabi', sowing_period='October - November', icon='🌾'),
        Crop(name='Gram (Chickpea)', season='Rabi', sowing_period='October - November', icon='🌱'),
        Crop(name='Mustard', season='Rabi', sowing_period='October - November', icon='🌼'),
        Crop(name='Linseed', season='Rabi', sowing_period='October - November', icon='🌿'),
        Crop(name='Peas', season='Rabi', sowing_period='October - November', icon='🫛'),
        Crop(name='Sunflower', season='Rabi', sowing_period='November - December', icon='🌻'),
        # Zaid
        Crop(name='Watermelon', season='Zaid', sowing_period='March - April', icon='🍉'),
        Crop(name='Muskmelon', season='Zaid', sowing_period='March - April', icon='🍈'),
        Crop(name='Cucumber', season='Zaid', sowing_period='March - April', icon='🥒'),
        Crop(name='Moong (Green Gram)', season='Zaid', sowing_period='March - April', icon='🌱'),
        Crop(name='Bitter Gourd', season='Zaid', sowing_period='March - April', icon='🥒'),
    ]

    db.session.add_all(crops)
    db.session.commit()
    print(f"[OK] Seeded {len(crops)} crops into database.")

    # Also seed demo farmer with lands
    seed_demo_farmer()


def seed_demo_farmer():
    """Seed a demo farmer with sample lands for testing."""
    if Farmer.query.count() > 0:
        return

    # Create demo farmer (login: 9999999999 / 1234)
    farmer = Farmer(
        name='Rajesh Kumar',
        mobile='9999999999',
        preferred_language='en',
        total_land_acres=8.5
    )
    farmer.set_password('1234')
    db.session.add(farmer)
    db.session.flush()  # get farmer.id

    # Create sample lands
    lands = [
        Land(farmer_id=farmer.id, land_uid='LND-00001',
             village='Rampur', district='Varanasi', state='Uttar Pradesh',
             area_acres=2.0, latitude=25.3176, longitude=82.9739),
        Land(farmer_id=farmer.id, land_uid='LND-00002',
             village='Shivpur', district='Varanasi', state='Uttar Pradesh',
             area_acres=1.5, latitude=25.2854, longitude=82.9916),
        Land(farmer_id=farmer.id, land_uid='LND-00003',
             village='Kotwa', district='Chandauli', state='Uttar Pradesh',
             area_acres=1.5, latitude=25.2584, longitude=83.2632),
        Land(farmer_id=farmer.id, land_uid='LND-00004',
             village='Hubli', district='Dharwad', state='Karnataka',
             area_acres=2.0, latitude=15.3647, longitude=75.1240),
        Land(farmer_id=farmer.id, land_uid='LND-00005',
             village='Gadag', district='Gadag', state='Karnataka',
             area_acres=1.5, latitude=15.4315, longitude=75.6355),
    ]

    db.session.add_all(lands)
    db.session.commit()
    print(f"[OK] Seeded demo farmer (mobile: 9999999999, password: 1234) with {len(lands)} lands.")

