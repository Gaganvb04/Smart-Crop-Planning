/**
 * Voice Module - Speech-to-Text & Text-to-Speech
 * Uses browser Web Speech API (no external service)
 */

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
let recognition = null;

/**
 * Voice input for a form field
 * @param {string} inputId - ID of the input field to fill
 * @param {function} callback - Optional callback after recognition
 */
function voiceInput(inputId, callback) {
    if (!SpeechRecognition) {
        alert('Voice input not supported in this browser. Use Chrome or Edge.');
        return;
    }

    recognition = new SpeechRecognition();
    const lang = localStorage.getItem('language') || 'en';

    // Set language for recognition
    const langMap = { 'en': 'en-IN', 'hi': 'hi-IN', 'kn': 'kn-IN' };
    recognition.lang = langMap[lang] || 'en-IN';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    // Visual feedback
    const voiceButtons = document.querySelectorAll('.btn-voice');
    voiceButtons.forEach(btn => btn.classList.add('listening'));

    recognition.onresult = (event) => {
        const text = event.results[0][0].transcript;
        const input = document.getElementById(inputId);
        if (input) {
            input.value = text;
            input.dispatchEvent(new Event('input'));
        }
        voiceButtons.forEach(btn => btn.classList.remove('listening'));
        if (callback) callback(text);
    };

    recognition.onerror = (event) => {
        console.error('Voice error:', event.error);
        voiceButtons.forEach(btn => btn.classList.remove('listening'));
        if (event.error === 'not-allowed') {
            alert('Please allow microphone access.');
        }
    };

    recognition.onend = () => {
        voiceButtons.forEach(btn => btn.classList.remove('listening'));
    };

    recognition.start();
}

/**
 * Text-to-Speech output
 * @param {string} text - Text to speak
 */
function speak(text) {
    if (!window.speechSynthesis) {
        console.warn('TTS not supported');
        return;
    }

    // Cancel any ongoing speech
    window.speechSynthesis.cancel();

    const utterance = new SpeechSynthesisUtterance(text);
    const lang = localStorage.getItem('language') || 'en';
    const langMap = { 'en': 'en-IN', 'hi': 'hi-IN', 'kn': 'kn-IN' };

    utterance.lang = langMap[lang] || 'en-IN';
    utterance.rate = 0.9;
    utterance.pitch = 1.0;

    window.speechSynthesis.speak(utterance);
}

/**
 * Stop voice recognition
 */
function stopVoice() {
    if (recognition) {
        recognition.stop();
    }
    window.speechSynthesis.cancel();
}
