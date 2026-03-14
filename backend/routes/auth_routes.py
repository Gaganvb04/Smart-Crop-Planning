from flask import Blueprint, request, jsonify, session
from services.farmer_service import FarmerService

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/api/register', methods=['POST'])
def register():
    """Register a new farmer."""
    data = request.get_json()
    if not data:
        return jsonify({'success': False, 'errors': ['No data provided']}), 400

    farmer, errors = FarmerService.register(data)
    if errors:
        return jsonify({'success': False, 'errors': errors}), 400

    session['farmer_id'] = farmer.id
    session['farmer_name'] = farmer.name
    session['language'] = farmer.preferred_language

    return jsonify({
        'success': True,
        'message': 'Registration successful',
        'farmer': farmer.to_dict()
    }), 201


@auth_bp.route('/api/login', methods=['POST'])
def login():
    """Login a farmer."""
    data = request.get_json()
    if not data:
        return jsonify({'success': False, 'error': 'No data provided'}), 400

    mobile = data.get('mobile', '')
    password = data.get('password', '')

    farmer, error = FarmerService.login(mobile, password)
    if error:
        return jsonify({'success': False, 'error': error}), 401

    session['farmer_id'] = farmer.id
    session['farmer_name'] = farmer.name
    session['language'] = farmer.preferred_language

    return jsonify({
        'success': True,
        'message': 'Login successful',
        'farmer': farmer.to_dict()
    })


@auth_bp.route('/api/logout', methods=['POST'])
def logout():
    """Logout a farmer."""
    session.clear()
    return jsonify({'success': True, 'message': 'Logged out successfully'})


@auth_bp.route('/api/me', methods=['GET'])
def get_current_farmer():
    """Get the current logged-in farmer."""
    farmer_id = session.get('farmer_id')
    if not farmer_id:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401

    farmer = FarmerService.get_farmer(farmer_id)
    if not farmer:
        session.clear()
        return jsonify({'success': False, 'error': 'Farmer not found'}), 404

    return jsonify({
        'success': True,
        'farmer': farmer.to_dict()
    })


@auth_bp.route('/api/farmer/update', methods=['PUT'])
def update_farmer():
    """Update farmer profile."""
    farmer_id = session.get('farmer_id')
    if not farmer_id:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401

    data = request.get_json()
    farmer, error = FarmerService.update_farmer(farmer_id, data)
    if error:
        return jsonify({'success': False, 'error': error}), 400

    return jsonify({
        'success': True,
        'farmer': farmer.to_dict()
    })
