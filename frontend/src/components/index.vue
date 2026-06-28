<template>
    <div class="login-page-container d-flex align-items-center justify-content-center py-5">
        <div class="form-card-wrapper w-100 px-3" style="max-width: 480px;">
            <!-- Brand Logo Header -->
            <div class="d-flex align-items-center justify-content-center gap-2 mb-4 fade-in-up">
                <div class="logo-box shadow-sm text-white">
                    <i class="bi bi-shield-plus fs-3"></i>
                </div>
                <span class="fs-3 fw-bold text-dark tracking-tight"> HMS Portal </span>
            </div>

            <!-- Login/Register Main Card -->
            <div class="card shadow-lg border-0 rounded-4 overflow-hidden fade-in-up">
                <!-- Visual Banner at Top of Card -->
                <div class="card-banner-img-wrapper position-relative">
                    <img src="/hospital_banner.png" alt="Hospital Care Center" class="img-fluid w-100 card-banner-img">
                    <div class="banner-gradient-overlay"></div>
                </div>

                <!-- Nav Tabs -->
                <div class="card-header bg-white p-0 border-bottom">
                    <div class="d-flex text-center">
                        <button class="tab-button w-50 py-3 fw-bold btn rounded-0"
                                :class="{active: view === 'login'}"
                                @click="view = 'login'">
                            <i class="bi bi-box-arrow-in-right me-2"></i>Sign In
                        </button>
                        <button class="tab-button w-50 py-3 fw-bold btn rounded-0"
                                :class="{active: view === 'register'}"
                                @click="view = 'register'">
                            <i class="bi bi-person-plus me-2"></i>Register
                        </button>
                    </div>
                </div>

                <div class="card-body p-4 p-md-5 bg-white">
                    <h4 class="mb-2 fw-bold text-dark font-heading">
                        {{ view === 'login' ? 'Welcome Back!' : 'Create Patient Account' }}
                    </h4>
                    <p class="text-muted small mb-4">
                        {{ view === 'login' ? 'Please log in to your designated portal.' : 'Sign up to manage and book your doctor visits.' }}
                    </p>

                    <!-- Alerts -->
                    <div v-if="error" class="alert alert-danger mb-4 shadow-sm border-0">
                        <i class="bi bi-exclamation-triangle-fill fs-5"></i>
                        <div>{{ error }}</div>
                    </div>
                    <div v-if="success" class="alert alert-success mb-4 shadow-sm border-0">
                        <i class="bi bi-check-circle-fill fs-5"></i>
                        <div>{{ success }}</div>
                    </div>

                    <!-- Login Form -->
                    <form v-if="view === 'login'" @submit.prevent="login" class="d-flex flex-column gap-3">
                        <div class="form-group-custom">
                            <label class="form-label text-secondary small fw-bold">Email Address</label>
                            <div class="input-icon-wrapper">
                                <input type="email" class="form-control" v-model="loginForm.email" placeholder="" required autocomplete="email">
                            </div>
                        </div>

                        <div class="form-group-custom">
                            <label class="form-label text-secondary small fw-bold">Password</label>
                            <div class="input-icon-wrapper">
                                <input type="password" class="form-control" v-model="loginForm.password" placeholder="" required autocomplete="current-password">
                            </div>
                        </div>

                        <button type="submit" class="btn btn-primary w-100 py-3 fs-6 rounded-3 mt-3 shadow-sm fw-bold">
                            <i class="bi bi-box-arrow-in-right me-2"></i>Access Portal
                        </button>
                    </form>

                    <!-- Registration Form -->
                    <form v-if="view === 'register'" @submit.prevent="register" class="d-flex flex-column gap-3">
                        <div class="form-group-custom">
                            <label class="form-label text-secondary small fw-bold">Full Name</label>
                            <div class="input-icon-wrapper">
                                <input type="text" class="form-control" v-model="registerForm.username" required autocomplete="name">
                            </div>
                        </div>

                        <div class="form-group-custom">
                            <label class="form-label text-secondary small fw-bold">Email Address</label>
                            <div class="input-icon-wrapper">
                                <input type="email" class="form-control" v-model="registerForm.email" required autocomplete="email">
                            </div>
                        </div>

                        <div class="form-group-custom">
                            <label class="form-label text-secondary small fw-bold">Phone Number</label>
                            <div class="input-icon-wrapper">
                                <input type="text" class="form-control" v-model="registerForm.contact" pattern="[0-9]+" minlength="7" required autocomplete="tel">
                            </div>
                        </div>

                        <div class="form-group-custom">
                            <label class="form-label text-secondary small fw-bold">Home Address</label>
                            <div class="input-icon-wrapper">
                                <input type="text" class="form-control" v-model="registerForm.address" autocomplete="street-address">
                            </div>
                        </div>

                        <div class="form-group-custom">
                            <label class="form-label text-secondary small fw-bold">Create Password</label>
                            <div class="input-icon-wrapper">
                                <input type="password" class="form-control" v-model="registerForm.password" minlength="6" required autocomplete="new-password">
                            </div>
                        </div>

                        <button type="submit" class="btn btn-success w-100 py-3 fs-6 rounded-3 mt-3 shadow-sm fw-bold">
                            <i class="bi bi-person-plus me-2"></i>Create Account
                        </button>
                    </form>
                </div>
            </div>
            
            <!-- Footer -->
            <div class="text-center mt-4 text-muted small">
                <span>© 2026 CareSync Systems • Patient & Provider Portal</span>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            view: 'login', error: '', success: '',
            loginForm: { email: '', password: '' },
            registerForm: { username: '', email: '', password: '', contact: '', address: '' }
        }
    },
    methods: {
        showMsg(type, msg) {
            if (type === 'success') {
                this.success = msg;
                setTimeout(() => { if (this.success === msg) this.success = ''; }, 5000);
            } else {
                this.error = msg;
                setTimeout(() => { if (this.error === msg) this.error = ''; }, 5000);
            }
        },
        async login() {
            try {
                const res = await fetch('http://127.0.0.1:5000/api/login', {
                    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(this.loginForm)
                });
                const data = await res.json();
                
                if (res.ok) {
                    localStorage.setItem('access_token', data.access_token);
                    localStorage.setItem('role', data.role);
                    localStorage.setItem('username', data.username);
                    this.showMsg('success', 'Login Successful!');
                    setTimeout(() => {
                        if (data.role === 'Admin') window.location.href = 'admin/admin_dashboard.html';
                        if (data.role === 'Doctor') window.location.href = 'doctor/doctor_dashboard.html';
                        if (data.role === 'Patient') window.location.href = 'patient/patient_dashboard.html';
                    }, 500);
                } else { this.showMsg('error', data.message); }
            } catch { this.showMsg('error', 'Network Error'); }
        },
        async register() {
            try {
                const res = await fetch('http://127.0.0.1:5000/api/register', {
                    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(this.registerForm)
                });
                if (res.ok) { this.showMsg('success', 'Registered! Please log in.'); this.view = 'login'; }
                else { const data = await res.json(); this.showMsg('error', data.message); }
            } catch { this.showMsg('error', 'Network Error'); }
        }
    }
}
</script>

<style scoped>
.login-page-container {
    min-height: 100vh;
    width: 100%;
    background: radial-gradient(circle at 10% 20%, rgba(4, 120, 87, 0.05) 0%, transparent 90%),
                radial-gradient(circle at 90% 80%, rgba(20, 184, 166, 0.08) 0%, transparent 90%),
                linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); /* Elegant pastel green gradient */
}

.logo-box {
    width: 44px;
    height: 44px;
    background: linear-gradient(135deg, #4f46e5 0%, #0ea5e9 100%);
    border-radius: 12px;
    display: grid;
    place-items: center;
}

.card-banner-img-wrapper {
    height: 180px;
    overflow: hidden;
}

.card-banner-img {
    height: 100%;
    object-fit: cover;
    object-position: center;
}

.banner-gradient-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, rgba(30, 41, 59, 0.1), rgba(255, 255, 255, 1));
}

.tab-button {
    border: none;
    background: #ffffff;
    color: #64748b;
    transition: var(--transition-smooth);
    border-bottom: 2.5px solid transparent;
}

.tab-button.active {
    color: #4f46e5;
    border-bottom: 2.5px solid #4f46e5 !important;
    background-color: rgba(79, 70, 229, 0.02) !important;
}

.input-icon-wrapper {
    position: relative;
}

.input-icon {
    position: absolute;
    left: 14px;
    top: 50%;
    transform: translateY(-50%);
    color: #94a3b8;
    font-size: 16px;
}

.input-icon-wrapper .form-control {
    background-color: #f8fafc;
    border-color: #e2e8f0;
}

.input-icon-wrapper .form-control:focus {
    background-color: #ffffff;
    border-color: #4f46e5 !important;
}

.form-group-custom {
    display: flex;
    flex-direction: column;
}

.tracking-tight {
    letter-spacing: -0.03em;
}

/* Animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.fade-in-up {
    animation: fadeInUp 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
</style>
