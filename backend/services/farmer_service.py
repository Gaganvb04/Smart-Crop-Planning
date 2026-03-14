from models import db, Farmer
from utils.validation import validate_farmer_data, validate_mobile, sanitize_input


class FarmerService:

    @staticmethod
    def register(data):
        """Register a new farmer."""
        errors = validate_farmer_data(data)
        if errors:
            return None, errors

        _, mobile = validate_mobile(data['mobile'])

        # Check if mobile already exists
        existing = Farmer.query.filter_by(mobile=mobile).first()
        if existing:
            return None, ["A farmer with this mobile number already exists"]

        farmer = Farmer(
            name=sanitize_input(data['name']),
            mobile=mobile,
            preferred_language=data.get('preferred_language', 'en'),
            total_land_acres=float(data.get('total_land_acres', 0))
        )
        farmer.set_password(data['password'])

        db.session.add(farmer)
        db.session.commit()

        return farmer, []

    @staticmethod
    def login(mobile, password):
        """Authenticate a farmer."""
        valid, result = validate_mobile(mobile)
        if not valid:
            return None, result

        farmer = Farmer.query.filter_by(mobile=result).first()
        if not farmer or not farmer.check_password(password):
            return None, "Invalid mobile number or password"

        return farmer, None

    @staticmethod
    def get_farmer(farmer_id):
        """Get farmer by ID."""
        return Farmer.query.get(farmer_id)

    @staticmethod
    def update_farmer(farmer_id, data):
        """Update farmer details."""
        farmer = Farmer.query.get(farmer_id)
        if not farmer:
            return None, "Farmer not found"

        if 'name' in data:
            farmer.name = sanitize_input(data['name'])
        if 'preferred_language' in data:
            farmer.preferred_language = data['preferred_language']
        if 'total_land_acres' in data:
            farmer.total_land_acres = float(data['total_land_acres'])

        db.session.commit()
        return farmer, None
