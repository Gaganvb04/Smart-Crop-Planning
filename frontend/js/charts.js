/**
 * Charts Module - Chart.js rendering for analytics
 */

// Color palette for charts
const CHART_COLORS = [
    '#2E7D32', '#4CAF50', '#81C784',
    '#FF8F00', '#FFB300', '#FFD54F',
    '#1565C0', '#42A5F5', '#90CAF9',
    '#E53935', '#EF5350', '#EF9A9A',
    '#00796B', '#26A69A', '#80CBC4'
];

const SEASON_COLORS = {
    'Kharif': '#2E7D32',
    'Rabi': '#1565C0',
    'Zaid': '#E65100'
};

// Cache for chart instances (to destroy before recreating)
const chartInstances = {};

/**
 * Render a thick bar chart
 */
function renderBarChart(canvasId, labels, data, label = 'Acres') {
    destroyChart(canvasId);

    const ctx = document.getElementById(canvasId);
    if (!ctx) return;

    chartInstances[canvasId] = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: label,
                data: data,
                backgroundColor: data.map((_, i) => CHART_COLORS[i % CHART_COLORS.length]),
                borderRadius: 8,
                borderWidth: 0,
                barThickness: 35,
                maxBarThickness: 50
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: {
                    backgroundColor: '#1A2E1A',
                    padding: 12,
                    titleFont: { size: 14 },
                    bodyFont: { size: 13 }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: { color: '#E0E0E0' },
                    ticks: { font: { size: 12 } },
                    title: { display: true, text: label, font: { size: 13 } }
                },
                x: {
                    grid: { display: false },
                    ticks: { font: { size: 11 }, maxRotation: 45 }
                }
            }
        }
    });
}

/**
 * Render a pie / doughnut chart
 */
function renderPieChart(canvasId, labels, data) {
    destroyChart(canvasId);

    const ctx = document.getElementById(canvasId);
    if (!ctx) return;

    const colors = labels.map((l, i) =>
        SEASON_COLORS[l] || CHART_COLORS[i % CHART_COLORS.length]
    );

    chartInstances[canvasId] = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: colors,
                borderWidth: 3,
                borderColor: '#ffffff',
                hoverOffset: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 16,
                        font: { size: 13 },
                        usePointStyle: true
                    }
                },
                tooltip: {
                    backgroundColor: '#1A2E1A',
                    padding: 12,
                    callbacks: {
                        label: function (ctx) {
                            const total = ctx.dataset.data.reduce((a, b) => a + b, 0);
                            const pct = total > 0 ? ((ctx.parsed / total) * 100).toFixed(1) : 0;
                            return `${ctx.label}: ${ctx.parsed.toFixed(1)} acres (${pct}%)`;
                        }
                    }
                }
            }
        }
    });
}

/**
 * Render district chart for crop detail
 */
function renderDistrictChart(districtBreakdown) {
    const labels = Object.keys(districtBreakdown);
    const data = Object.values(districtBreakdown);
    renderBarChart('district-chart', labels, data, 'Acres');
}

/**
 * Render season chart for crop detail
 */
function renderSeasonChart(seasonBreakdown) {
    const labels = Object.keys(seasonBreakdown);
    const data = Object.values(seasonBreakdown);
    renderPieChart('season-chart', labels, data);
}

/**
 * Destroy a chart instance if it exists
 */
function destroyChart(canvasId) {
    if (chartInstances[canvasId]) {
        chartInstances[canvasId].destroy();
        delete chartInstances[canvasId];
    }
}
