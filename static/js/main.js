const API_URL = '/api';

const auth = {
    async login(email, password) {
        const formData = new FormData();
        formData.append('username', email);
        formData.append('password', password);
        
        const response = await fetch('/login', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        if (response.ok) {
            localStorage.setItem('token', data.access_token);
            window.location.href = '/dashboard';
        }
        return data;
    },
    logout() {
        localStorage.removeItem('token');
        window.location.href = '/';
    },
    getToken() {
        return localStorage.getItem('token');
    }
};

const resumes = {
    async upload(file) {
        const formData = new FormData();
        formData.append('file', file);
        
        const response = await fetch(`${API_URL}/upload-resume`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${auth.getToken()}`
            },
            body: formData
        });
        return await response.json();
    },
    async list() {
        const response = await fetch(`${API_URL}/resumes`, {
            headers: {
                'Authorization': `Bearer ${auth.getToken()}`
            }
        });
        return await response.json();
    },
    async analyze(resumeId) {
        const response = await fetch(`${API_URL}/analyze-resume/${resumeId}`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${auth.getToken()}`
            }
        });
        return await response.json();
    }
};

// UI Handling
document.addEventListener('DOMContentLoaded', () => {
    const token = auth.getToken();
    const guestNav = document.getElementById('guest-nav');
    const userNav = document.getElementById('user-nav');
    
    if (token) {
        if (guestNav) guestNav.style.display = 'none';
        if (userNav) userNav.style.display = 'flex';
    }

    const logoutBtn = document.getElementById('logout-btn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', () => auth.logout());
    }
});
