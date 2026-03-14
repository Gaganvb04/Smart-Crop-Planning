import math


def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two GPS coordinates in kilometers.
    Used to detect duplicate/overlapping land entries.
    """
    R = 6371  # Earth's radius in kilometers

    lat1, lon1, lat2, lon2 = map(math.radians, [
        float(lat1), float(lon1), float(lat2), float(lon2)
    ])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))

    return R * c


def is_duplicate_location(lat1, lon1, lat2, lon2, threshold_km=0.1):
    """
    Check if two locations are within the threshold distance.
    Default threshold: 100 meters (0.1 km).
    """
    if None in (lat1, lon1, lat2, lon2):
        return False
    distance = haversine_distance(lat1, lon1, lat2, lon2)
    return distance <= threshold_km


def format_coordinates(lat, lng):
    """Format coordinates for display."""
    if lat is None or lng is None:
        return "Location not set"
    lat_dir = 'N' if float(lat) >= 0 else 'S'
    lng_dir = 'E' if float(lng) >= 0 else 'W'
    return f"{abs(float(lat)):.4f}°{lat_dir}, {abs(float(lng)):.4f}°{lng_dir}"
