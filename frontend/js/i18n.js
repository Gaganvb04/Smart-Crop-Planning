/**
 * i18n Module - Multi-language support
 * Supports: English (en), Hindi (hi), Kannada (kn)
 */

const translations = {
    en: {
        app_name: 'Smart Crop Planning',
        continue: 'Continue →',
        login: '🔑 Login',
        register: '📝 Register',
        logout: '🚪 Logout',
        dashboard: '🏠 Dashboard',
        land: '📍 Land',
        crops: '🌱 Crops',
        analytics: '📊 Analytics',
        mobile_number: '📱 Mobile Number',
        password: '🔒 Password',
        farmer_name: '👤 Farmer Name',
        preferred_language: '🌐 Preferred Language',
        total_land: '🌍 Total Land (Acres)',
        welcome: '🙏 Welcome!',
        dashboard_subtitle: 'Your farming overview at a glance',
        total_lands: 'Total Lands',
        total_acres: 'Total Acres',
        crops_mapped: 'Crops Mapped',
        unmapped: 'Unmapped',
        register_title: '📝 Farmer Registration',
        register_subtitle: 'Create your account to start planning',
        land_subtitle: 'Register and manage your land locations',
        crop_search_subtitle: 'Search crops by text or voice',
        analytics_subtitle: 'Visual market trends and crop analysis',
        no_account: 'No account?',
        register_here: 'Register here',
        have_account: 'Already have an account?',
        login_here: 'Login here',
        welcome_voice: 'Welcome to Smart Crop Planning. Please log in or register.',
        register_help_voice: 'Fill in your details to register as a farmer.'
    },
    hi: {
        app_name: 'स्मार्ट फसल योजना',
        continue: 'आगे बढ़ें →',
        login: '🔑 लॉगिन',
        register: '📝 पंजीकरण',
        logout: '🚪 लॉगआउट',
        dashboard: '🏠 डैशबोर्ड',
        land: '📍 भूमि',
        crops: '🌱 फसलें',
        analytics: '📊 विश्लेषण',
        mobile_number: '📱 मोबाइल नंबर',
        password: '🔒 पासवर्ड',
        farmer_name: '👤 किसान का नाम',
        preferred_language: '🌐 पसंदीदा भाषा',
        total_land: '🌍 कुल भूमि (एकड़)',
        welcome: '🙏 स्वागत है!',
        dashboard_subtitle: 'आपकी खेती का अवलोकन',
        total_lands: 'कुल भूमि',
        total_acres: 'कुल एकड़',
        crops_mapped: 'मैप की गई फसलें',
        unmapped: 'बिना मैप',
        register_title: '📝 किसान पंजीकरण',
        register_subtitle: 'योजना शुरू करने के लिए पंजीकरण करें',
        land_subtitle: 'अपनी भूमि स्थान दर्ज करें',
        crop_search_subtitle: 'फसल खोजें - टेक्स्ट या आवाज़ से',
        analytics_subtitle: 'बाज़ार रुझान और फसल विश्लेषण',
        no_account: 'खाता नहीं है?',
        register_here: 'यहाँ पंजीकरण करें',
        have_account: 'पहले से खाता है?',
        login_here: 'यहाँ लॉगिन करें',
        welcome_voice: 'स्मार्ट फसल योजना में आपका स्वागत है। कृपया लॉगिन या पंजीकरण करें।',
        register_help_voice: 'किसान के रूप में पंजीकरण के लिए अपना विवरण भरें।'
    },
    kn: {
        app_name: 'ಸ್ಮಾರ್ಟ್ ಬೆಳೆ ಯೋಜನೆ',
        continue: 'ಮುಂದುವರಿಸಿ →',
        login: '🔑 ಲಾಗಿನ್',
        register: '📝 ನೋಂದಣಿ',
        logout: '🚪 ಲಾಗ್‌ಔಟ್',
        dashboard: '🏠 ಡ್ಯಾಶ್‌ಬೋರ್ಡ್',
        land: '📍 ಭೂಮಿ',
        crops: '🌱 ಬೆಳೆಗಳು',
        analytics: '📊 ವಿಶ್ಲೇಷಣೆ',
        mobile_number: '📱 ಮೊಬೈಲ್ ಸಂಖ್ಯೆ',
        password: '🔒 ಪಾಸ್‌ವರ್ಡ್',
        farmer_name: '👤 ರೈತರ ಹೆಸರು',
        preferred_language: '🌐 ಆದ್ಯತೆಯ ಭಾಷೆ',
        total_land: '🌍 ಒಟ್ಟು ಭೂಮಿ (ಎಕರೆ)',
        welcome: '🙏 ಸ್ವಾಗತ!',
        dashboard_subtitle: 'ನಿಮ್ಮ ಕೃಷಿ ಅವಲೋಕನ',
        total_lands: 'ಒಟ್ಟು ಭೂಮಿ',
        total_acres: 'ಒಟ್ಟು ಎಕರೆ',
        crops_mapped: 'ಮ್ಯಾಪ್ ಮಾಡಿದ ಬೆಳೆಗಳು',
        unmapped: 'ಮ್ಯಾಪ್ ಆಗಿಲ್ಲ',
        register_title: '📝 ರೈತ ನೋಂದಣಿ',
        register_subtitle: 'ಯೋಜನೆ ಪ್ರಾರಂಭಿಸಲು ನೋಂದಣಿ ಮಾಡಿ',
        land_subtitle: 'ನಿಮ್ಮ ಭೂಮಿ ಸ್ಥಳಗಳನ್ನು ನೋಂದಿಸಿ',
        crop_search_subtitle: 'ಬೆಳೆ ಹುಡುಕಿ - ಪಠ್ಯ ಅಥವಾ ಧ್ವನಿ',
        analytics_subtitle: 'ಮಾರುಕಟ್ಟೆ ಪ್ರವೃತ್ತಿ ಮತ್ತು ಬೆಳೆ ವಿಶ್ಲೇಷಣೆ',
        no_account: 'ಖಾತೆ ಇಲ್ಲವೇ?',
        register_here: 'ಇಲ್ಲಿ ನೋಂದಣಿ ಮಾಡಿ',
        have_account: 'ಈಗಾಗಲೇ ಖಾತೆ ಇದೆಯೇ?',
        login_here: 'ಇಲ್ಲಿ ಲಾಗಿನ್ ಮಾಡಿ',
        welcome_voice: 'ಸ್ಮಾರ್ಟ್ ಬೆಳೆ ಯೋಜನೆಗೆ ಸ್ವಾಗತ. ದಯವಿಟ್ಟು ಲಾಗಿನ್ ಅಥವಾ ನೋಂದಣಿ ಮಾಡಿ.',
        register_help_voice: 'ರೈತರಾಗಿ ನೋಂದಣಿ ಮಾಡಲು ನಿಮ್ಮ ವಿವರಗಳನ್ನು ಭರ್ತಿ ಮಾಡಿ.'
    }
};

let currentLanguage = 'en';

/**
 * Set the current language and update all translatable elements
 */
function setLanguage(lang) {
    currentLanguage = lang;
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (translations[lang] && translations[lang][key]) {
            el.textContent = translations[lang][key];
        }
    });
}

/**
 * Get a translation for a key
 */
function getTranslation(key) {
    return (translations[currentLanguage] && translations[currentLanguage][key])
        || (translations['en'] && translations['en'][key])
        || key;
}
