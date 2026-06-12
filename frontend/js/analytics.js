/**
 * Analytics Module - Fetch and process analytics data
 */

/**
 * Load analytics for a specific crop
 */
async function loadCropAnalytics(cropId) {
    try {
        const res = await api.get(`/api/analytics/crop/${cropId}`);
        if (res.success) {
            return res.analytics;
        }
    } catch (e) {
        console.error('Failed to load crop analytics:', e);
    }
    return null;
}

/**
 * Load summary analytics for all crops
 */
async function loadAllCropsSummary() {
    try {
        const res = await api.get('/api/analytics/summary');
        if (res.success) {
            return res.summary;
        }
    } catch (e) {
        console.error('Failed to load summary:', e);
    }
    return [];
}

/**
 * Get market trend description for voice output
 */
function getMarketTrendDescription(analytics) {
    if (!analytics) return '';

    const crop = analytics.crop;
    const trend = analytics.market_trend;
    const totalAcres = analytics.total_acres;
    const districts = Object.keys(analytics.district_breakdown);

    let desc = `${crop.name} has ${totalAcres.toFixed(1)} total acres across ${districts.length} districts. `;
    desc += `Market status: ${trend.label}. ${trend.advice}`;

    return desc;
}
