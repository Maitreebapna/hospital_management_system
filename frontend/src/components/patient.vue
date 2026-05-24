<template>
    <div class="dashboard-container fade-in-up">
        <!-- Modern Left Sidebar Navigation -->
        <div class="dashboard-sidebar text-white">
            <div>
                <!-- Brand logo area -->
                <div class="sidebar-brand">
                    <div>
                        <span class="fw-bold tracking-tight text-white fs-4 d-block">HMS Patient</span>
                        <span class="text-muted small" style="font-size: 11px !important;">Patient Portal</span>
                    </div>
                </div>
                
                <!-- Menu Links -->
                <div class="sidebar-nav-menu">
                    <button class="sidebar-nav-btn" :class="{active: currentTab === 'booking'}" @click="currentTab = 'booking'">
                        <i class="bi bi-calendar-plus"></i>
                        <span>Book Appointment</span>
                    </button>
                    <button class="sidebar-nav-btn" :class="{active: currentTab === 'records'}" @click="currentTab = 'records'">
                        <i class="bi bi-file-earmark-medical"></i>
                        <span>Medical Records</span>
                    </button>
                </div>
            </div>
            
            <!-- User Profile & Logout at Bottom -->
            <div class="sidebar-footer-profile">
                <div class="d-flex align-items-center gap-2">
                    <div class="sidebar-avatar">P</div>
                    <div>
                        <span class="text-white fw-bold d-block small">Patient Portal</span>
                        <span class="text-muted small d-block" style="font-size: 10px !important;">Active Session</span>
                    </div>
                </div>
                <button class="btn-sidebar-logout" @click="logout" title="Logout Session">
                    <i class="bi bi-box-arrow-right"></i>
                </button>
            </div>
        </div>

        <!-- Main Dashboard Viewport -->
        <div class="dashboard-main-content">
            <!-- Notifications overlay -->
            <transition name="fade">
                <div v-if="error" class="alert alert-danger shadow-sm border-0 mb-4">{{ error }}</div>
            </transition>
            <transition name="fade">
                <div v-if="success" class="alert alert-success shadow-sm border-0 mb-4">{{ success }}</div>
            </transition>

            <!-- -----------------------------------------
                 TAB 1: BOOKING & PROFILE
            ------------------------------------------ -->
            <div v-show="currentTab === 'booking'" class="fade-in-up">
                <div class="d-flex justify-content-between align-items-center mb-4">
                    <h3 class="mb-0 fw-bold font-heading text-primary">Book New Appointment</h3>
                    <span class="text-muted small fw-medium">Real-time scheduling</span>
                </div>

                <div class="row g-4">
                    <!-- Profile Update Form -->
                    <div class="col-md-5">
                        <div class="card shadow-sm border-0">
                            <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
                                <i class="bi bi-person-gear text-primary fs-5"></i>
                                <h5 class="mb-0 fw-bold text-dark">Update Contact Details</h5>
                            </div>
                            <div class="card-body p-4 bg-white">
                                <form @submit.prevent="updateProfile" class="d-flex flex-column gap-3">
                                    <div>
                                        <label class="form-label mb-1 text-secondary small fw-bold">Phone Number</label>
                                        <div class="input-icon-wrapper">
                                            <i class="bi bi-telephone input-icon"></i>
                                            <input type="text" class="form-control" v-model="profileForm.contact" placeholder="Enter phone number">
                                        </div>
                                    </div>
                                    <div>
                                        <label class="form-label mb-1 text-secondary small fw-bold">Home Address</label>
                                        <div class="input-icon-wrapper">
                                            <i class="bi bi-geo-alt input-icon"></i>
                                            <input type="text" class="form-control" v-model="profileForm.address" placeholder="Enter home address">
                                        </div>
                                    </div>
                                    <button class="btn btn-primary w-100 py-3 rounded-3 mt-2 shadow-sm fw-bold">
                                        <i class="bi bi-check2-circle me-1"></i>Save Profile Changes
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>

                    <!-- Search and Select Specialist -->
                    <div class="col-md-7">
                        <div class="card shadow-sm border-0">
                            <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
                                <i class="bi bi-search-heart text-primary fs-5"></i>
                                <h5 class="mb-0 fw-bold text-dark">Find a Medical Specialist</h5>
                            </div>
                            <div class="card-body p-4 bg-white">
                                <div class="input-group mb-4 shadow-sm rounded-3 overflow-hidden">
                                    <span class="input-group-text bg-light border-1"><i class="bi bi-search text-muted"></i></span>
                                    <input type="text" class="form-control" v-model="searchQuery" placeholder="Search by name, specialization, day..." @keyup.enter="searchDoctors">
                                    <button class="btn btn-primary" @click="searchDoctors">Search</button>
                                </div>
                                
                                <!-- Search Doctor Card Grid -->
                                <div class="doctor-results-list pe-1" style="max-height: 400px; overflow-y: auto;">
                                    <div class="card border mb-3 doctor-search-card shadow-none transition-all" v-for="doc in searchResults" :key="doc.id">
                                        <div class="card-body p-3 d-flex justify-content-between align-items-center gap-3">
                                            <div class="d-flex align-items-center gap-2" style="min-width: 0;">
                                                <div class="bg-primary-light text-primary rounded-circle d-flex align-items-center justify-content-center" style="width: 44px; height: 44px; flex-shrink: 0;">
                                                    <i class="bi bi-person-fill fs-5"></i>
                                                </div>
                                                <div style="min-width: 0;">
                                                    <h6 class="mb-0 fw-bold text-dark text-truncate">{{ doc.name }}</h6>
                                                    <span class="badge bg-secondary font-heading rounded-pill text-truncate my-1 d-inline-block">{{ doc.specialization }} Department</span>
                                                    <span class="text-muted d-block small" style="font-size: 12px !important;"><i class="bi bi-clock me-1"></i>{{ doc.availability }} ({{ doc.time_availability }})</span>
                                                </div>
                                            </div>
                                            <button class="btn btn-sm btn-primary rounded-pill px-3 py-1 flex-shrink-0" @click="selectDoctor(doc)">
                                                Select
                                            </button>
                                        </div>
                                    </div>
                                    <div v-if="searchResults.length === 0" class="text-center text-muted py-5">
                                        <i class="bi bi-people fs-2 d-block mb-2"></i>
                                        No doctors found matching query.
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Confirm Appointment Booking Panel -->
                        <transition name="slide-up">
                            <div class="card border-0 shadow-lg mt-4 booking-card" v-if="targetDoctor">
                                <div class="card-header bg-primary text-white d-flex justify-content-between align-items-center py-3">
                                    <h5 class="mb-0 fw-bold"><i class="bi bi-calendar-plus me-2"></i>Book: {{ targetDoctor.name }}</h5>
                                    <button type="button" class="btn-close btn-close-white" @click="targetDoctor = null"></button>
                                </div>
                                <div class="card-body p-4 bg-white">
                                    <div class="alert alert-info border-0 rounded-3 mb-4 text-center">
                                        Doctor Availability:<br><b class="fs-6">{{ targetDoctor.availability }} | {{ targetDoctor.time_availability }}</b>
                                    </div>
                                    <form @submit.prevent="bookAppt" class="d-flex flex-column gap-3">
                                        <div>
                                            <label class="form-label text-secondary small fw-bold">Select Date</label>
                                            <input type="date" class="form-control" v-model="bookForm.date" required>
                                        </div>
                                        
                                        <div>
                                            <label class="form-label text-secondary small fw-bold">Preferred Time Slot</label>
                                            <div class="input-icon-wrapper">
                                                <i class="bi bi-clock input-icon"></i>
                                                <input type="text" class="form-control" v-model="bookForm.time_slot" placeholder="e.g. 10:30 AM" required>
                                            </div>
                                        </div>
                                        
                                        <button class="btn btn-primary w-100 py-3 rounded-3 mt-2 shadow">
                                            <i class="bi bi-check-circle me-1"></i>Confirm Appointment
                                        </button>
                                    </form>
                                </div>
                            </div>
                        </transition>
                    </div>
                </div>
            </div>

            <!-- -----------------------------------------
                 TAB 2: MEDICAL RECORDS TIMELINE
            ------------------------------------------ -->
            <div v-show="currentTab === 'records'" class="fade-in-up">
                <div class="d-flex justify-content-between align-items-center mb-4">
                    <h3 class="mb-0 fw-bold font-heading text-primary">Your Medical Records</h3>
                    <button class="btn btn-sm btn-outline-primary px-3 rounded-pill" @click="exportData">
                        <i class="bi bi-download me-1"></i>Export CSV
                    </button>
                </div>

                <div class="row g-4">
                    <div class="col-12">
                        <div class="card shadow-sm border-0">
                            <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
                                <i class="bi bi-file-earmark-medical text-primary fs-5"></i>
                                <h5 class="mb-0 fw-bold text-dark">Clinical Visits History</h5>
                            </div>
                            <div class="card-body p-4 bg-white" style="max-height: 700px; overflow-y: auto;">
                                <div v-if="history.length === 0" class="text-center text-muted py-5">
                                    <i class="bi bi-folder2-open fs-2 d-block mb-2"></i>
                                    You have no medical records yet.
                                </div>

                                <div class="timeline-container d-flex flex-column gap-3">
                                    <template v-for="h in history" :key="h.id">
                                        <div class="card border mb-3 record-card rounded-3 shadow-none transition-all" v-if="h.status !== 'Cancelled'">
                                            <div class="card-body p-4 bg-white">
                                                <div class="d-flex justify-content-between align-items-start gap-2 mb-3">
                                                    <div>
                                                        <h5 class="fw-bold text-dark mb-1">{{ h.date }}</h5>
                                                        <span class="text-muted small"><i class="bi bi-clock me-1"></i>{{ h.time_slot }} • <i class="bi bi-person-fill text-muted me-1"></i>{{ h.doctor_name }}</span>
                                                    </div>
                                                    <span class="badge rounded-pill px-3 py-2" 
                                                          :class="h.status === 'Completed' ? 'bg-success-subtle text-success border border-success-subtle' : 'bg-primary-subtle text-primary border border-primary-subtle'">
                                                        {{ h.status }}
                                                    </span>
                                                </div>
                                                
                                                <div v-if="h.treatment" class="treatment-box p-3 rounded bg-light border-start border-primary border-4">
                                                    <p class="mb-2"><strong class="text-primary small text-uppercase">Diagnosis:</strong> <span class="text-dark d-block fw-medium mt-1">{{ h.treatment.diagnosis }}</span></p>
                                                    <p class="mb-0"><strong class="text-primary small text-uppercase">Prescription:</strong> <span class="text-dark d-block fw-medium mt-1">{{ h.treatment.prescription }}</span></p>
                                                </div>
                                                
                                                <div v-if="h.status === 'Booked'" class="mt-3 pt-3 border-top d-flex gap-2">
                                                    <button class="btn btn-sm btn-warning flex-grow-1 py-2 text-white" @click="openReschedule(h)">Reschedule</button>
                                                    <button class="btn btn-sm btn-outline-danger flex-grow-1 py-2" @click="cancelAppt(h.id)">Cancel</button>
                                                </div>
                                            </div>
                                        </div>
                                    </template>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Reschedule Overlay Modal -->
        <transition name="fade">
            <div v-if="rescheduleData" class="reschedule-overlay d-flex align-items-center justify-content-center">
                <div class="card border-0 shadow-lg p-2 reschedule-card rounded-4">
                    <div class="card-header bg-transparent border-0 pt-4 pb-2 d-flex justify-content-between align-items-center">
                        <h5 class="mb-0 fw-bold text-dark">Reschedule Appointment</h5>
                        <button type="button" class="btn-close" @click="rescheduleData = null"></button>
                    </div>
                    <div class="card-body">
                        <p class="text-muted small mb-4">Doctor: {{ rescheduleData.doctor_name }}</p>
                        <form @submit.prevent="submitReschedule" class="d-flex flex-column gap-3">
                            <div>
                                <label class="form-label fw-bold text-muted small">New Date</label>
                                <input type="date" class="form-control py-2 px-3" v-model="rescheduleForm.date" required>
                            </div>
                            
                            <div>
                                <label class="form-label fw-bold text-muted small">New Time Slot</label>
                                <input type="text" class="form-control py-2 px-3" v-model="rescheduleForm.time_slot" placeholder="e.g. 10:00 AM" required>
                            </div>
                            
                            <button type="submit" class="btn btn-warning w-100 py-3 text-white fw-bold mt-2 shadow">Confirm Changes</button>
                        </form>
                    </div>
                </div>
            </div>
        </transition>

        <!-- Floating Theme Customizer -->
        <button class="theme-customizer-trigger" @click="showThemeCustomizer = !showThemeCustomizer" title="Customize Theme">
            <i class="bi bi-gear-fill"></i>
        </button>
        <transition name="fade">
            <div class="theme-customizer-panel" v-if="showThemeCustomizer">
                <h6 class="fw-bold mb-2 small text-uppercase text-muted">Accent Color</h6>
                <div class="color-dot-container">
                    <div class="color-dot" 
                         v-for="color in themePresets" 
                         :key="color.name"
                         :style="{backgroundColor: color.hex}"
                         :class="{active: activeAccent === color.name}"
                         @click="setAccent(color.name)"
                         :title="color.label">
                        <i class="bi bi-check-lg" v-if="activeAccent === color.name"></i>
                    </div>
                </div>
                <button class="mode-toggle-btn" @click="toggleDarkMode">
                    <span class="small">{{ isDarkMode ? 'Light Mode' : 'Dark Mode' }}</span>
                    <i class="bi" :class="isDarkMode ? 'bi-sun-fill text-warning' : 'bi-moon-fill text-primary'"></i>
                </button>
            </div>
        </transition>
    </div>
</template>

<script>
export default {
    data() {
        return {
            token: localStorage.getItem('access_token'),
            error: '', success: '',
            searchQuery: '', searchResults: [], targetDoctor: null, departments: [],
            bookForm: { date: '', time_slot: '' },
            profileForm: { contact: '', address: '' },
            history: [],
            rescheduleData: null, rescheduleForm: { date: '', time_slot: '' },
            currentTab: 'booking',
            showThemeCustomizer: false,
            isDarkMode: false,
            activeAccent: 'sky',
            themePresets: [
                { name: 'indigo', label: 'Indigo', hex: '#6366f1' },
                { name: 'teal', label: 'Teal', hex: '#14b8a6' },
                { name: 'sky', label: 'Sky Blue', hex: '#0ea5e9' },
                { name: 'emerald', label: 'Emerald Mint', hex: '#10b981' },
                { name: 'rose', label: 'Sunset Rose', hex: '#f43f5e' },
                { name: 'amber', label: 'Sunset Gold', hex: '#f59e0b' },
                { name: 'purple', label: 'Royal Purple', hex: '#8b5cf6' }
            ]
        }
    },
    methods: {
        authHeader() { return { 'Authorization': 'Bearer ' + this.token, 'Content-Type': 'application/json' }; },
        logout() { localStorage.clear(); window.location.href = '/index.html'; },
        
        selectDoctor(doc) {
            this.targetDoctor = doc;
        },
        
        async fetchHistory() {
            const res = await fetch('http://127.0.0.1:5000/api/patient/history', { headers: this.authHeader() });
            if (res.ok) this.history = await res.json();
        },
        async fetchDepartments() {
            const res = await fetch('http://127.0.0.1:5000/api/departments');
            if (res.ok) this.departments = await res.json();
        },
        showMsg(type, msg) {
            if (type === 'success') {
                this.success = msg;
                setTimeout(() => { if (this.success === msg) this.success = ''; }, 5000);
            } else {
                this.error = msg;
                setTimeout(() => { if (this.error === msg) this.error = ''; }, 5000);
            }
        },
        async searchDoctors() {
            this.error = '';
            const res = await fetch('http://127.0.0.1:5000/api/patient/doctors/search?q=' + this.searchQuery, { headers: this.authHeader() });
            if (res.ok) this.searchResults = await res.json();
        },
        async bookAppt() {
            const selectedDate = new Date(this.bookForm.date);
            const today = new Date();
            today.setHours(0, 0, 0, 0);
            if (selectedDate < today) {
                this.showMsg('error', "Sorry, you cannot book an appointment for a past date.");
                return;
            }

            const payload = { doctor_id: this.targetDoctor.id, ...this.bookForm };
            const res = await fetch('http://127.0.0.1:5000/api/patient/appointments/book', {
                method: 'POST', headers: this.authHeader(), body: JSON.stringify(payload)
            });
            const data = await res.json();

            if (res.ok) {
                this.showMsg('success', "Booked successfully!");
                this.targetDoctor = null;
                this.bookForm = { date: '', time_slot: '' };
                this.fetchHistory(); 
            } else {
                this.showMsg('error', data.message);
            }
        },
        async exportData() {
            const res = await fetch('http://127.0.0.1:5000/api/patient/export-history', { method: 'POST', headers: this.authHeader() });
            if (res.ok) {
                const blob = await res.blob();
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'Patient_Medical_History_Report.csv';
                document.body.appendChild(a);
                a.click();
                a.remove();
                this.showMsg('success', "Medical Record downloaded!");
            } else {
                this.showMsg('error', "Failed to download medical records.");
            }
        },
        async updateProfile() {
            const res = await fetch('http://127.0.0.1:5000/api/patient/profile', {
                method: 'PUT', headers: this.authHeader(), body: JSON.stringify(this.profileForm)
            });
            if (res.ok) { 
                this.showMsg('success', "Profile updated."); 
                this.profileForm = { contact: '', address: '' }; 
            }
        },
        openReschedule(h) {
            this.rescheduleData = h;
            this.rescheduleForm.date = h.date;
            this.rescheduleForm.time_slot = h.time_slot;
            this.error = ''; this.success = '';
        },
        async submitReschedule() {
            const selectedDate = new Date(this.rescheduleForm.date);
            const today = new Date();
            today.setHours(0, 0, 0, 0);
            if (selectedDate < today) {
                this.showMsg('error', "Sorry, you cannot reschedule to a past date.");
                return;
            }

            const res = await fetch('http://127.0.0.1:5000/api/patient/appointment/' + this.rescheduleData.id, {
                method: 'PATCH',
                headers: this.authHeader(),
                body: JSON.stringify({
                    date: this.rescheduleForm.date,
                    time_slot: this.rescheduleForm.time_slot
                })
            });
            if (res.ok) {
                this.showMsg('success', "Appointment rescheduled!");
                this.rescheduleData = null;
                this.fetchHistory();
            } else {
                const data = await res.json();
                this.showMsg('error', "Error: " + data.message);
            }
        },
        async cancelAppt(id) {
            if (confirm("Are you sure you want to cancel this appointment?")) {
                const res = await fetch('http://127.0.0.1:5000/api/patient/appointment/' + id, {
                    method: 'PATCH', headers: this.authHeader(), body: JSON.stringify({ status: 'Cancelled' })
                });
                if (res.ok) { this.showMsg('success', "Appointment cancelled!"); this.fetchHistory(); }
            }
        },
        loadTheme() {
            const darkMode = localStorage.getItem('theme-dark') === 'true';
            this.isDarkMode = darkMode;
            if (darkMode) {
                document.body.classList.add('dark-theme');
            } else {
                document.body.classList.remove('dark-theme');
            }

            const accent = localStorage.getItem('theme-accent') || this.activeAccent;
            this.activeAccent = accent;
            this.applyAccentClass(accent);
        },
        toggleDarkMode() {
            this.isDarkMode = !this.isDarkMode;
            localStorage.setItem('theme-dark', this.isDarkMode);
            if (this.isDarkMode) {
                document.body.classList.add('dark-theme');
            } else {
                document.body.classList.remove('dark-theme');
            }
        },
        setAccent(accent) {
            this.activeAccent = accent;
            localStorage.setItem('theme-accent', accent);
            this.applyAccentClass(accent);
        },
        applyAccentClass(accent) {
            const prefixes = ['accent-indigo', 'accent-teal', 'accent-sky', 'accent-emerald', 'accent-rose', 'accent-amber', 'accent-purple'];
            prefixes.forEach(p => document.body.classList.remove(p));
            document.body.classList.add('accent-' + accent);
        }
    },
    mounted() {
        this.loadTheme();
        if (!this.token || localStorage.getItem('role') !== 'Patient') this.logout();
        else { this.fetchHistory(); this.fetchDepartments(); this.searchDoctors(); }
    }
}
</script>

<style scoped>
.doctor-search-card {
    transition: var(--transition-smooth);
}

.doctor-search-card:hover {
    border-color: var(--theme-primary) !important;
    transform: translateY(-1.5px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02) !important;
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
    padding-left: 42px;
}

.treatment-box {
    border-left: 4px solid var(--theme-primary) !important;
}

.reschedule-overlay {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background-color: rgba(15, 23, 42, 0.5);
    z-index: 9999;
    backdrop-filter: blur(4px);
}
.reschedule-card {
    min-width: 350px;
    max-width: 450px;
    width: 100%;
}

/* Animations */
.slide-up-enter-active, .slide-up-leave-active { transition: all 0.3s ease; }
.slide-up-enter-from, .slide-up-leave-to { opacity: 0; transform: translateY(10px); }
.fade-enter-active, .fade-leave-active { transition: opacity 0.3s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
</style>
