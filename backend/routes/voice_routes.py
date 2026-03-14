from flask import Blueprint, request, jsonify

voice_bp = Blueprint('voice', __name__)


@voice_bp.route('/api/voice/process', methods=['POST'])
def process_voice_input():
    """
    Process voice input text (after browser speech-to-text).
    The actual speech recognition happens in the browser via Web Speech API.
    This endpoint processes the recognized text for commands.
    """
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'success': False, 'error': 'No voice text provided'}), 400

    text = data['text'].strip().lower()
    context = data.get('context', 'general')

    # Determine action based on voice input context
    response = {
        'success': True,
        'recognized_text': text,
        'action': None,
        'data': None
    }

    if context == 'crop_search':
        # Voice input for crop search
        response['action'] = 'search_crop'
        response['data'] = {'search_term': text}

    elif context == 'navigation':
        # Voice navigation commands
        nav_commands = {
            'dashboard': '/pages/dashboard.html',
            'home': '/',
            'land': '/pages/land.html',
            'crop': '/pages/crop-search.html',
            'analytics': '/pages/analytics.html',
            'search': '/pages/crop-search.html',
            'register': '/pages/register.html',
        }
        for key, url in nav_commands.items():
            if key in text:
                response['action'] = 'navigate'
                response['data'] = {'url': url}
                break

    elif context == 'form_fill':
        response['action'] = 'fill_field'
        response['data'] = {'value': text}

    return jsonify(response)


@voice_bp.route('/api/voice/tts-config', methods=['GET'])
def get_tts_config():
    """Get text-to-speech configuration for the current language."""
    lang = request.args.get('lang', 'en')

    lang_voices = {
        'en': {'lang': 'en-IN', 'rate': 0.9, 'pitch': 1.0},
        'hi': {'lang': 'hi-IN', 'rate': 0.85, 'pitch': 1.0},
        'kn': {'lang': 'kn-IN', 'rate': 0.85, 'pitch': 1.0}
    }

    config = lang_voices.get(lang, lang_voices['en'])
    return jsonify({'success': True, 'config': config})
