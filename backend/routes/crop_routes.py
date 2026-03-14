from flask import Blueprint, request, jsonify
from services.crop_service import CropService

crop_bp = Blueprint('crop', __name__)


@crop_bp.route('/api/crops', methods=['GET'])
def get_crops():
    """Get all crops, optionally filtered by season."""
    season = request.args.get('season')
    crops = CropService.get_all_crops(season)
    return jsonify({
        'success': True,
        'crops': [crop.to_dict() for crop in crops]
    })


@crop_bp.route('/api/crops/search', methods=['GET'])
def search_crops():
    """Search crops by name (text or voice search)."""
    query = request.args.get('q', '')
    if not query:
        return jsonify({'success': True, 'crops': []})

    crops = CropService.search_crops(query)
    return jsonify({
        'success': True,
        'crops': [crop.to_dict() for crop in crops],
        'query': query
    })


@crop_bp.route('/api/crops/<int:crop_id>', methods=['GET'])
def get_crop(crop_id):
    """Get a specific crop."""
    crop = CropService.get_crop(crop_id)
    if not crop:
        return jsonify({'success': False, 'error': 'Crop not found'}), 404

    return jsonify({
        'success': True,
        'crop': crop.to_dict()
    })


@crop_bp.route('/api/crop-mapping', methods=['POST'])
def map_crop():
    """Map a crop to a land."""
    data = request.get_json()
    if not data:
        return jsonify({'success': False, 'errors': ['No data provided']}), 400

    mapping, errors = CropService.map_crop_to_land(data)
    if errors:
        return jsonify({'success': False, 'errors': errors}), 400

    return jsonify({
        'success': True,
        'message': 'Crop mapped successfully',
        'mapping': mapping.to_dict()
    }), 201


@crop_bp.route('/api/crop-mapping/<int:mapping_id>', methods=['DELETE'])
def remove_crop_mapping(mapping_id):
    """Remove a crop-land mapping."""
    success, error = CropService.remove_crop_mapping(mapping_id)
    if not success:
        return jsonify({'success': False, 'error': error}), 404

    return jsonify({
        'success': True,
        'message': 'Crop mapping removed successfully'
    })
