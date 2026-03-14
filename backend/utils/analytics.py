from .constants import MARKET_THRESHOLDS


def classify_market_trend(total_acres):
    """
    Classify market opportunity based on total acres under a crop.
    Returns: 'high_supply' (red), 'balanced' (yellow), or 'high_opportunity' (green)
    """
    if total_acres >= MARKET_THRESHOLDS['high_supply']:
        return {
            'level': 'high_supply',
            'color': 'red',
            'label': 'High Supply - Oversaturated',
            'icon': '🔴',
            'advice': 'Consider alternative crops. Market may be oversaturated.'
        }
    elif total_acres >= MARKET_THRESHOLDS['balanced']:
        return {
            'level': 'balanced',
            'color': 'yellow',
            'label': 'Balanced Supply',
            'icon': '🟡',
            'advice': 'Market is balanced. Moderate competition expected.'
        }
    else:
        return {
            'level': 'high_opportunity',
            'color': 'green',
            'label': 'High Opportunity',
            'icon': '🟢',
            'advice': 'Low competition. Good opportunity to grow this crop!'
        }


def aggregate_by_district(land_crop_data):
    """
    Aggregate total acres by district for a specific crop.
    Input: list of (district, area_acres) tuples
    Returns: dict of {district: total_acres}
    """
    district_totals = {}
    for district, acres in land_crop_data:
        district = str(district)
        district_totals[district] = district_totals.get(district, 0) + float(acres)
    return district_totals


def aggregate_by_season(land_crop_data):
    """
    Aggregate total acres by season for a specific crop.
    Input: list of (season, area_acres) tuples
    Returns: dict of {season: total_acres}
    """
    season_totals = {}
    for season, acres in land_crop_data:
        season = str(season)
        season_totals[season] = season_totals.get(season, 0) + float(acres)
    return season_totals
