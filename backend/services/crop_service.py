from models import db, Crop, LandCrop, Land
from utils.validation import validate_crop_mapping


class CropService:

    @staticmethod
    def get_all_crops(season=None):
        """Get all crops, optionally filtered by season."""
        query = Crop.query
        if season:
            query = query.filter_by(season=season)
        return query.order_by(Crop.season, Crop.name).all()

    @staticmethod
    def search_crops(search_term):
        """Search crops by name (text or voice input)."""
        if not search_term:
            return []
        return Crop.query.filter(
            Crop.name.ilike(f'%{search_term}%')
        ).order_by(Crop.name).all()

    @staticmethod
    def get_crop(crop_id):
        """Get a single crop by ID."""
        return Crop.query.get(crop_id)

    @staticmethod
    def map_crop_to_land(data):
        """Map a crop to a land for a specific season/year."""
        errors = validate_crop_mapping(data)
        if errors:
            return None, errors

        land_id = int(data['land_id'])
        crop_id = int(data['crop_id'])
        season = data['season']
        year = int(data['year'])

        # Check if land exists
        land = Land.query.get(land_id)
        if not land:
            return None, ["Land not found"]

        # Check if crop exists
        crop = Crop.query.get(crop_id)
        if not crop:
            return None, ["Crop not found"]

        # Check for existing mapping (one crop per land per season per year)
        existing = LandCrop.query.filter_by(
            land_id=land_id, season=season, year=year
        ).first()
        if existing:
            return None, [f"This land already has a crop mapped for {season} {year}"]

        mapping = LandCrop(
            land_id=land_id,
            crop_id=crop_id,
            season=season,
            year=year
        )

        db.session.add(mapping)
        db.session.commit()

        return mapping, []

    @staticmethod
    def remove_crop_mapping(mapping_id):
        """Remove a crop-land mapping."""
        mapping = LandCrop.query.get(mapping_id)
        if not mapping:
            return False, "Mapping not found"

        db.session.delete(mapping)
        db.session.commit()
        return True, None
