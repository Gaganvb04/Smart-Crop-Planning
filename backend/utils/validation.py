import re
from .constants import SEASONS


def validate_mobile(mobile):
    """Validate Indian mobile number (10 digits)."""
    if not mobile:
        return False, "Mobile number is required"
    mobile = re.sub(r'[\s\-\+]', '', str(mobile))
    if mobile.startswith('91') and len(mobile) == 12:
        mobile = mobile[2:]
    if not re.match(r'^[6-9]\d{9}$', mobile):
        return False, "Invalid mobile number. Must be 10 digits starting with 6-9"
    return True, mobile


def validate_farmer_data(data):
    """Validate farmer registration data."""
    errors = []

    if not data.get('name') or len(data['name'].strip()) < 2:
        errors.append("Name must be at least 2 characters")

    valid, result = validate_mobile(data.get('mobile', ''))
    if not valid:
        errors.append(result)

    if not data.get('password') or len(data['password']) < 4:
        errors.append("Password must be at least 4 characters")

    return errors


def validate_land_data(data):
    """Validate land registration data."""
    errors = []

    if not data.get('village') or len(data['village'].strip()) < 2:
        errors.append("Village name is required")

    if not data.get('district') or len(data['district'].strip()) < 2:
        errors.append("District name is required")

    if not data.get('state') or len(data['state'].strip()) < 2:
        errors.append("State name is required")

    area = data.get('area_acres')
    try:
        area = float(area)
        if area <= 0 or area > 1000:
            errors.append("Land area must be between 0 and 1000 acres")
    except (TypeError, ValueError):
        errors.append("Valid land area in acres is required")

    return errors


def validate_crop_mapping(data):
    """Validate crop mapping data."""
    errors = []

    if not data.get('land_id'):
        errors.append("Land selection is required")

    if not data.get('crop_id'):
        errors.append("Crop selection is required")

    season = data.get('season')
    if season not in SEASONS:
        errors.append(f"Season must be one of: {', '.join(SEASONS)}")

    year = data.get('year')
    try:
        year = int(year)
        if year < 2020 or year > 2030:
            errors.append("Year must be between 2020 and 2030")
    except (TypeError, ValueError):
        errors.append("Valid year is required")

    return errors


def sanitize_input(text):
    """Sanitize text input to prevent injection."""
    if not text:
        return ''
    text = str(text).strip()
    text = re.sub(r'[<>"\';]', '', text)
    return text
