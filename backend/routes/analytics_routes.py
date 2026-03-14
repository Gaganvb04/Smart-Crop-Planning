from flask import Blueprint, request, jsonify, session
from services.analytics_service import AnalyticsService

analytics_bp = Blueprint('analytics', __name__)


@analytics_bp.route('/api/analytics/crop/<int:crop_id>', methods=['GET'])
def get_crop_analytics(crop_id):
    """Get full analytics for a specific crop."""
    result = AnalyticsService.get_crop_analytics(crop_id)
    if not result:
        return jsonify({'success': False, 'error': 'Crop not found'}), 404

    return jsonify({
        'success': True,
        'analytics': result
    })


@analytics_bp.route('/api/analytics/summary', methods=['GET'])
def get_all_crops_summary():
    """Get summary analytics for all crops."""
    summary = AnalyticsService.get_all_crops_summary()
    return jsonify({
        'success': True,
        'summary': summary
    })


@analytics_bp.route('/api/analytics/farmer', methods=['GET'])
def get_farmer_analytics():
    """Get analytics for the logged-in farmer."""
    farmer_id = session.get('farmer_id')
    if not farmer_id:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401

    result = AnalyticsService.get_farmer_analytics(farmer_id)
    return jsonify({
        'success': True,
        'analytics': result
    })
