-- Smart Crop Planning - Performance Indexes

USE smart_crop_planning;

-- Fast lookup of lands by farmer
CREATE INDEX idx_lands_farmer_id ON lands(farmer_id);

-- Fast crop search by name
CREATE INDEX idx_crops_name ON crops(name);

-- Fast crop search by season
CREATE INDEX idx_crops_season ON crops(season);

-- Fast aggregation by district
CREATE INDEX idx_lands_district ON lands(district);

-- Fast aggregation by state
CREATE INDEX idx_lands_state ON lands(state);

-- Fast lookup of crop mappings
CREATE INDEX idx_land_crops_crop_id ON land_crops(crop_id);
CREATE INDEX idx_land_crops_season ON land_crops(season);
CREATE INDEX idx_land_crops_year ON land_crops(year);

-- Fast farmer lookup by mobile number (login)
CREATE INDEX idx_farmers_mobile ON farmers(mobile);
