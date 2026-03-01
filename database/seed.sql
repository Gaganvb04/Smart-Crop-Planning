-- Smart Crop Planning - Sample Seed Data

USE smart_crop_planning;

-- =============================================
-- Seed Crops Master Data
-- =============================================
INSERT INTO crops (name, season, sowing_period, icon) VALUES
-- Kharif Crops (June-October)
('Rice', 'Kharif', 'June - July', '🌾'),
('Maize', 'Kharif', 'June - July', '🌽'),
('Cotton', 'Kharif', 'April - May', '☁️'),
('Sugarcane', 'Kharif', 'February - March', '🎋'),
('Groundnut', 'Kharif', 'June - July', '🥜'),
('Soybean', 'Kharif', 'June - July', '🫘'),
('Jowar (Sorghum)', 'Kharif', 'June - July', '🌾'),
('Bajra (Pearl Millet)', 'Kharif', 'June - July', '🌾'),
('Tur (Pigeon Pea)', 'Kharif', 'June - July', '🌱'),
('Ragi (Finger Millet)', 'Kharif', 'June - July', '🌾'),

-- Rabi Crops (October-March)
('Wheat', 'Rabi', 'October - November', '🌾'),
('Barley', 'Rabi', 'October - November', '🌾'),
('Gram (Chickpea)', 'Rabi', 'October - November', '🌱'),
('Mustard', 'Rabi', 'October - November', '🌼'),
('Linseed', 'Rabi', 'October - November', '🌿'),
('Peas', 'Rabi', 'October - November', '🫛'),
('Sunflower', 'Rabi', 'November - December', '🌻'),

-- Zaid Crops (March-June)
('Watermelon', 'Zaid', 'March - April', '🍉'),
('Muskmelon', 'Zaid', 'March - April', '🍈'),
('Cucumber', 'Zaid', 'March - April', '🥒'),
('Moong (Green Gram)', 'Zaid', 'March - April', '🌱'),
('Bitter Gourd', 'Zaid', 'March - April', '🥒');

-- =============================================
-- Seed Sample Farmer (password: farmer123)
-- =============================================
INSERT INTO farmers (name, mobile, password_hash, preferred_language, total_land_acres) VALUES
('Rajesh Kumar', '9876543210', 'pbkdf2:sha256:600000$salt$hash_placeholder', 'hi', 5.00),
('Anita Devi', '9876543211', 'pbkdf2:sha256:600000$salt$hash_placeholder', 'en', 3.50),
('Basavaraj Patil', '9876543212', 'pbkdf2:sha256:600000$salt$hash_placeholder', 'kn', 8.00);

-- =============================================
-- Seed Sample Lands
-- =============================================
INSERT INTO lands (farmer_id, land_uid, village, district, state, area_acres, latitude, longitude) VALUES
(1, 'LND-00001', 'Rampur', 'Varanasi', 'Uttar Pradesh', 2.00, 25.3176, 82.9739),
(1, 'LND-00002', 'Shivpur', 'Varanasi', 'Uttar Pradesh', 1.50, 25.2854, 82.9916),
(1, 'LND-00003', 'Kotwa', 'Chandauli', 'Uttar Pradesh', 1.50, 25.2584, 83.2632),
(2, 'LND-00004', 'Lalganj', 'Pratapgarh', 'Uttar Pradesh', 2.00, 25.8960, 81.9468),
(2, 'LND-00005', 'Sarai', 'Pratapgarh', 'Uttar Pradesh', 1.50, 25.8833, 81.9541),
(3, 'LND-00006', 'Hubli', 'Dharwad', 'Karnataka', 3.00, 15.3647, 75.1240),
(3, 'LND-00007', 'Gadag', 'Gadag', 'Karnataka', 2.50, 15.4315, 75.6355),
(3, 'LND-00008', 'Navalgund', 'Dharwad', 'Karnataka', 2.50, 15.5571, 75.3548);

-- =============================================
-- Seed Sample Land-Crop Mappings
-- =============================================
INSERT INTO land_crops (land_id, crop_id, season, year) VALUES
(1, 1, 'Kharif', 2025),   -- Rajesh: Rampur - Rice - Kharif
(2, 11, 'Rabi', 2025),    -- Rajesh: Shivpur - Wheat - Rabi
(3, 1, 'Kharif', 2025),   -- Rajesh: Kotwa - Rice - Kharif
(4, 11, 'Rabi', 2025),    -- Anita: Lalganj - Wheat - Rabi
(5, 13, 'Rabi', 2025),    -- Anita: Sarai - Gram - Rabi
(6, 3, 'Kharif', 2025),   -- Basavaraj: Hubli - Cotton - Kharif
(7, 2, 'Kharif', 2025),   -- Basavaraj: Gadag - Maize - Kharif
(8, 14, 'Rabi', 2025),    -- Basavaraj: Navalgund - Mustard - Rabi
(1, 11, 'Rabi', 2025),    -- Rajesh: Rampur - Wheat - Rabi (same land, different season)
(6, 11, 'Rabi', 2025);    -- Basavaraj: Hubli - Wheat - Rabi
