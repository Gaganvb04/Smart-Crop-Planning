from flask import Blueprint, request, jsonify, session
from services.land_service import LandService

land_bp = Blueprint('land', __name__)


@land_bp.route('/api/lands', methods=['GET'])
def get_lands():
    """Get all lands for the logged-in farmer."""
    farmer_id = session.get('farmer_id')
    if not farmer_id:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401

    lands = LandService.get_lands_by_farmer(farmer_id)
    return jsonify({
        'success': True,
        'lands': [land.to_dict() for land in lands]
    })


@land_bp.route('/api/lands', methods=['POST'])
def add_land():
    """Add a new land for the logged-in farmer."""
    farmer_id = session.get('farmer_id')
    if not farmer_id:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401

    data = request.get_json()
    if not data:
        return jsonify({'success': False, 'errors': ['No data provided']}), 400

    land, errors = LandService.add_land(farmer_id, data)
    if errors:
        return jsonify({'success': False, 'errors': errors}), 400

    return jsonify({
        'success': True,
        'message': 'Land added successfully',
        'land': land.to_dict()
    }), 201


@land_bp.route('/api/lands/<int:land_id>', methods=['GET'])
def get_land(land_id):
    """Get a specific land."""
    land = LandService.get_land(land_id)
    if not land:
        return jsonify({'success': False, 'error': 'Land not found'}), 404

    return jsonify({
        'success': True,
        'land': land.to_dict()
    })


@land_bp.route('/api/lands/<int:land_id>', methods=['PUT'])
def update_land(land_id):
    """Update a land entry."""
    data = request.get_json()
    land, error = LandService.update_land(land_id, data)
    if error:
        return jsonify({'success': False, 'error': error}), 400

    return jsonify({
        'success': True,
        'land': land.to_dict()
    })


@land_bp.route('/api/lands/<int:land_id>', methods=['DELETE'])
def delete_land(land_id):
    """Delete a land entry."""
    success, error = LandService.delete_land(land_id)
    if not success:
        return jsonify({'success': False, 'error': error}), 404

    return jsonify({
        'success': True,
        'message': 'Land deleted successfully'
    })
