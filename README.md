# 🌾 Smart Crop Planning & Market Trend Analysis

A web-based application that helps Indian farmers make data-driven crop decisions by analyzing season, location, land area, and market trends — with a simple, visual, multilingual, voice-enabled interface.

## ✨ Features

| Module | Description |
|---|---|
| 👤 User Management | Farmer registration & login (text + voice input) |
| 📍 Land Management | Multiple land locations with map-based GPS marking |
| 🌾 Crop Mapping | One crop per land per season (Kharif / Rabi / Zaid) |
| 🔍 Crop Research | Text + voice search with market trend indicators |
| 📊 Market Analytics | Bar charts, pie charts, traffic light indicators |
| 🎙️ Voice Support | Speech-to-text input & text-to-speech output |
| 🌐 Multi-Language | English, Hindi (हिन्दी), Kannada (ಕನ್ನಡ) |
| 🚦 Market Trends | Acre-based analysis (not farmer count) |
| 🔒 Duplication Prevention | Unique IDs, GPS proximity checks |

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python Flask, MySQL, SQLAlchemy |
| Frontend | HTML5, CSS3, JavaScript |
| Maps | Leaflet.js (OpenStreetMap) |
| Charts | Chart.js |
| Voice | Web Speech API |
| i18n | Custom JS translations |

## 📁 Project Structure

```
├── backend/
│   ├── app.py              # Flask application
│   ├── config.py           # MySQL configuration
│   ├── models/             # SQLAlchemy models
│   ├── routes/             # API endpoints
│   ├── services/           # Business logic
│   └── utils/              # Helpers & constants
├── frontend/
│   ├── index.html          # Landing + login
│   ├── pages/              # Dashboard, land, crops, analytics
│   ├── css/                # Theme, main, mobile styles
│   ├── js/                 # API, auth, voice, map, charts, i18n
│   └── assets/             # Icons, images, audio
├── database/
│   ├── schema.sql          # MySQL table creation
│   ├── seed.sql            # Sample data
│   └── indexes.sql         # Performance indexes
└── tests/                  # Test files
```

## 🚀 Setup

### Prerequisites
- Python 3.8+
- MySQL Server
- pip

### 1. Create MySQL Database
```sql
CREATE DATABASE smart_crop_planning;
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Database
Edit `backend/config.py` or set environment variables:
```bash
set MYSQL_HOST=localhost
set MYSQL_USER=root
set MYSQL_PASSWORD=yourpassword
set MYSQL_DB=smart_crop_planning
```

### 4. Run the Server
```bash
python backend/app.py
```

### 5. Open in Browser
```
http://localhost:5000
```

## 📱 Usage Flow

1. **Select Language** → English / Hindi / Kannada
2. **Register/Login** → Mobile number + password
3. **Add Land** → Village, district, state, acres, GPS location
4. **Map Crops** → Select land → choose crop → select season
5. **Search Crops** → Text or voice search
6. **View Analytics** → Charts, market trends, recommendations

## 📊 Market Trend Logic

| Indicator | Total Acres | Meaning |
|---|---|---|
| 🔴 Red | > 1000 | High Supply — avoid |
| 🟡 Yellow | 500 - 1000 | Balanced |
| 🟢 Green | < 500 | High Opportunity — grow this! |

## 👥 Team

Built as a Smart Crop Planning project for data-driven agriculture.