/**
 * Auth Helper - Login, logout, session check
 */

// Check if farmer is logged in (redirect to login if not)
(function checkAuth() {
    const publicPages = ['/', '/index.html'];
    const path = window.location.pathname;

    if (publicPages.includes(path) || path.includes('register.html')) {
        return; // login/register pages don't need auth
    }

    const farmer = localStorage.getItem('farmer');
    if (!farmer) {
        window.location.href = '/';
    }
})();

/**
 * Handle logout
 */
async function handleLogout() {
    try {
        await api.post('/api/logout', {});
    } catch (e) { }
    localStorage.removeItem('farmer');
    window.location.href = '/';
}

/**
 * Get current farmer data
 */
function getCurrentFarmer() {
    try {
        return JSON.parse(localStorage.getItem('farmer') || '{}');
    } catch (e) {
        return {};
    }
}
