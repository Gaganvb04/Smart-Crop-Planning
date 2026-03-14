from models import db, Crop, LandCrop, Land
from utils.analytics import classify_market_trend, aggregate_by_district, aggregate_by_season
from sqlalchemy import func


class AnalyticsService:

    @staticmethod
    def get_crop_analytics(crop_id):
        """
        Get full analytics for a specific crop:
        - Total acres
        - District-wise breakdown
        - Season-wise breakdown
        - Market trend classification
        """
        crop = Crop.query.get(crop_id)
        if not crop:
            return None

        # Total acres under this crop
        total_acres_result = db.session.query(
            func.sum(Land.area_acres)
        ).join(LandCrop, LandCrop.land_id == Land.id).filter(
            LandCrop.crop_id == crop_id
        ).scalar()
        total_acres = float(total_acres_result or 0)

        # District-wise breakdown
        district_data = db.session.query(
            Land.district, func.sum(Land.area_acres)
        ).join(LandCrop, LandCrop.land_id == Land.id).filter(
            LandCrop.crop_id == crop_id
        ).group_by(Land.district).all()
        district_breakdown = aggregate_by_district(district_data)

        # Season-wise breakdown
        season_data = db.session.query(
            LandCrop.season, func.sum(Land.area_acres)
        ).join(Land, LandCrop.land_id == Land.id).filter(
            LandCrop.crop_id == crop_id
        ).group_by(LandCrop.season).all()
        season_breakdown = aggregate_by_season(season_data)

        # Market trend
        market_trend = classify_market_trend(total_acres)

        return {
            'crop': crop.to_dict(),
            'total_acres': total_acres,
            'district_breakdown': district_breakdown,
            'season_breakdown': season_breakdown,
            'market_trend': market_trend
        }

    @staticmethod
    def get_all_crops_summary():
        """Get summary analytics for all crops."""
        results = db.session.query(
            Crop.id, Crop.name, Crop.icon, Crop.season,
            func.sum(Land.area_acres).label('total_acres'),
            func.count(LandCrop.id).label('mapping_count')
        ).outerjoin(LandCrop, LandCrop.crop_id == Crop.id
        ).outerjoin(Land, LandCrop.land_id == Land.id
        ).group_by(Crop.id, Crop.name, Crop.icon, Crop.season
        ).order_by(Crop.name).all()

        summary = []
        for row in results:
            total = float(row.total_acres or 0)
            summary.append({
                'crop_id': row.id,
                'name': row.name,
                'icon': row.icon,
                'season': row.season,
                'total_acres': total,
                'mapping_count': row.mapping_count,
                'market_trend': classify_market_trend(total)
            })

        return summary

    @staticmethod
    def get_farmer_analytics(farmer_id):
        """Get analytics for a specific farmer's lands and crops."""
        lands = Land.query.filter_by(farmer_id=farmer_id).all()

        total_land_acres = sum(float(l.area_acres) for l in lands)
        mapped_lands = 0
        crop_distribution = {}

        for land in lands:
            if land.crop_mappings:
                mapped_lands += 1
                for mapping in land.crop_mappings:
                    crop_name = mapping.crop.name if mapping.crop else 'Unknown'
                    if crop_name not in crop_distribution:
                        crop_distribution[crop_name] = 0
                    crop_distribution[crop_name] += float(land.area_acres)

        return {
            'total_lands': len(lands),
            'total_land_acres': total_land_acres,
            'mapped_lands': mapped_lands,
            'unmapped_lands': len(lands) - mapped_lands,
            'crop_distribution': crop_distribution
        }
