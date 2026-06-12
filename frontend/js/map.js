/**
 * Map Module - Leaflet.js integration for land location marking
 */

let landMap = null;
let landMarker = null;
let onLocationSelect = null;

/**
 * Initialize the land map
 * @param {string} containerId - Map container element ID
 * @param {function} onSelect - Callback when location is selected (lat, lng)
 */
function initLandMap(containerId, onSelect) {
    onLocationSelect = onSelect;

    // Default center: India
    landMap = L.map(containerId).setView([20.5937, 78.9629], 5);

    // OpenStreetMap tiles (free, no API key)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors',
        maxZoom: 19
    }).addTo(landMap);

    // Click on map to place marker
    landMap.on('click', function (e) {
        setMapMarker(e.latlng.lat, e.latlng.lng);
        if (onLocationSelect) {
            onLocationSelect(e.latlng.lat, e.latlng.lng);
        }
    });
}

/**
 * Set / move the marker on the map
 * @param {number} lat - Latitude
 * @param {number} lng - Longitude
 */
function setMapMarker(lat, lng) {
    if (!landMap) return;

    if (landMarker) {
        landMarker.setLatLng([lat, lng]);
    } else {
        landMarker = L.marker([lat, lng], {
            draggable: true
        }).addTo(landMap);

        // Update coordinates when marker is dragged
        landMarker.on('dragend', function (e) {
            const pos = e.target.getLatLng();
            if (onLocationSelect) {
                onLocationSelect(pos.lat, pos.lng);
            }
        });
    }

    landMap.setView([lat, lng], 14);
    landMarker.bindPopup(`📍 ${lat.toFixed(4)}, ${lng.toFixed(4)}`).openPopup();
}

/**
 * Get current GPS location
 * @param {function} callback - Callback with (lat, lng)
 */
function getGPSLocation(callback) {
    if (!navigator.geolocation) {
        alert('GPS not supported');
        return;
    }

    navigator.geolocation.getCurrentPosition(
        (pos) => {
            const lat = pos.coords.latitude;
            const lng = pos.coords.longitude;
            setMapMarker(lat, lng);
            if (callback) callback(lat, lng);
        },
        (err) => {
            console.error('GPS error:', err);
            alert('Unable to get location. Please mark on map.');
        },
        { enableHighAccuracy: true, timeout: 10000 }
    );
}
