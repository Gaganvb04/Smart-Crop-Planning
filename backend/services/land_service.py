from models import db, Land
from utils.validation import validate_land_data, sanitize_input
from utils.geo_utils import is_duplicate_location


class LandService:

    @staticmethod
    def add_land(farmer_id, data):
        """Add a new land for a farmer."""
        errors = validate_land_data(data)
        if errors:
            return None, errors

        lat = data.get('latitude')
        lng = data.get('longitude')

        # Check for duplicate land location
        if lat and lng:
            existing_lands = Land.query.filter_by(farmer_id=farmer_id).all()
            for existing in existing_lands:
                if is_duplicate_location(lat, lng, existing.latitude, existing.longitude):
                    return None, ["A land at this location already exists (within 100m)"]

        land = Land(
            farmer_id=farmer_id,
            land_uid=Land.generate_land_uid(),
            village=sanitize_input(data['village']),
            district=sanitize_input(data['district']),
            state=sanitize_input(data['state']),
            area_acres=float(data['area_acres']),
            latitude=float(lat) if lat else None,
            longitude=float(lng) if lng else None
        )

        db.session.add(land)
        db.session.commit()

        return land, []

    @staticmethod
    def get_lands_by_farmer(farmer_id):
        """Get all lands for a farmer."""
        return Land.query.filter_by(farmer_id=farmer_id).all()

    @staticmethod
    def get_land(land_id):
        """Get a single land by ID."""
        return Land.query.get(land_id)

    @staticmethod
    def update_land(land_id, data):
        """Update a land entry."""
        land = Land.query.get(land_id)
        if not land:
            return None, "Land not found"

        if 'village' in data:
            land.village = sanitize_input(data['village'])
        if 'district' in data:
            land.district = sanitize_input(data['district'])
        if 'state' in data:
            land.state = sanitize_input(data['state'])
        if 'area_acres' in data:
            land.area_acres = float(data['area_acres'])
        if 'latitude' in data:
            land.latitude = float(data['latitude']) if data['latitude'] else None
        if 'longitude' in data:
            land.longitude = float(data['longitude']) if data['longitude'] else None

        db.session.commit()
        return land, None

    @staticmethod
    def delete_land(land_id):
        """Delete a land entry."""
        land = Land.query.get(land_id)
        if not land:
            return False, "Land not found"

        db.session.delete(land)
        db.session.commit()
        return True, None
