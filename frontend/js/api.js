/**
 * API Helper - Backend API calls wrapper
 */
const API_BASE = '';

const api = {
    async get(url) {
        const res = await fetch(API_BASE + url, {
            method: 'GET',
            credentials: 'include',
            headers: { 'Content-Type': 'application/json' }
        });
        return await res.json();
    },

    async post(url, data) {
        const res = await fetch(API_BASE + url, {
            method: 'POST',
            credentials: 'include',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return await res.json();
    },

    async put(url, data) {
        const res = await fetch(API_BASE + url, {
            method: 'PUT',
            credentials: 'include',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return await res.json();
    },

    async delete(url) {
        const res = await fetch(API_BASE + url, {
            method: 'DELETE',
            credentials: 'include',
            headers: { 'Content-Type': 'application/json' }
        });
        return await res.json();
    }
};
