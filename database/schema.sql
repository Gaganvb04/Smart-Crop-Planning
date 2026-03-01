-- Smart Crop Planning - Database Schema (MySQL)

CREATE DATABASE IF NOT EXISTS smart_crop_planning;
USE smart_crop_planning;

-- =============================================
-- 1. Farmers Table
-- =============================================
CREATE TABLE IF NOT EXISTS farmers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    mobile VARCHAR(15) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    preferred_language VARCHAR(10) DEFAULT 'en',
    total_land_acres DECIMAL(10, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- =============================================
-- 2. Lands Table
-- =============================================
CREATE TABLE IF NOT EXISTS lands (
    id INT AUTO_INCREMENT PRIMARY KEY,
    farmer_id INT NOT NULL,
    land_uid VARCHAR(20) NOT NULL UNIQUE,
    village VARCHAR(100) NOT NULL,
    district VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    area_acres DECIMAL(10, 2) NOT NULL,
    latitude DECIMAL(10, 7),
    longitude DECIMAL(10, 7),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (farmer_id) REFERENCES farmers(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- =============================================
-- 3. Crops Master Table
-- =============================================
CREATE TABLE IF NOT EXISTS crops (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    season ENUM('Kharif', 'Rabi', 'Zaid') NOT NULL,
    sowing_period VARCHAR(100),
    icon VARCHAR(50) DEFAULT '🌾',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- =============================================
-- 4. Land-Crop Mapping Table
-- =============================================
CREATE TABLE IF NOT EXISTS land_crops (
    id INT AUTO_INCREMENT PRIMARY KEY,
    land_id INT NOT NULL,
    crop_id INT NOT NULL,
    season ENUM('Kharif', 'Rabi', 'Zaid') NOT NULL,
    year INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (land_id) REFERENCES lands(id) ON DELETE CASCADE,
    FOREIGN KEY (crop_id) REFERENCES crops(id) ON DELETE CASCADE,
    UNIQUE KEY unique_land_season_year (land_id, season, year)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
