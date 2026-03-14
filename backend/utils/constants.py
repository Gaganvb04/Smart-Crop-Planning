# Seasons
SEASONS = ['Kharif', 'Rabi', 'Zaid']

# Season months mapping
SEASON_MONTHS = {
    'Kharif': 'June - October',
    'Rabi': 'October - March',
    'Zaid': 'March - June'
}

# Market trend thresholds (in total acres)
MARKET_THRESHOLDS = {
    'high_supply': 1000,    # Above this = oversupply (red)
    'balanced': 500,        # Between balanced and high_supply = balanced (yellow)
    # Below balanced = high opportunity (green)
}

# Supported languages
LANGUAGES = {
    'en': 'English',
    'hi': 'हिन्दी',
    'kn': 'ಕನ್ನಡ'
}

# Default language
DEFAULT_LANGUAGE = 'en'

# Land proximity threshold (km) for duplicate detection
LAND_PROXIMITY_THRESHOLD_KM = 0.1  # 100 meters

# Indian states list
INDIAN_STATES = [
    'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar',
    'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana',
    'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala',
    'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya',
    'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
    'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
    'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'
]
