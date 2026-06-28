<template>
    <div class="dashboard-container fade-in-up">
        <!-- Modern Left Sidebar Navigation -->
        <div class="dashboard-sidebar text-white">
            <div>
                <!-- Brand logo area -->
                <div class="sidebar-brand">
                    <div>
                        <span class="fw-bold tracking-tight text-white fs-4 d-block">HMS Patient</span>
                        <span class="text-muted small" style="font-size: 11px !important;">{{ patientName }}'s Portal</span>
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
                    <div class="sidebar-avatar">{{ patientName.charAt(0).toUpperCase() }}</div>
                    <div>
                        <span class="text-white fw-bold d-block small">{{ patientName }} Portal</span>
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
                                            <input type="text" class="form-control" v-model="profileForm.contact" placeholder="Enter phone number">
                                        </div>
                                    </div>
                                    <div>
                                        <label class="form-label mb-1 text-secondary small fw-bold">Home Address</label>
                                        <div class="input-icon-wrapper">
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
                    <div class="d-flex gap-2">
                        <button class="btn btn-sm btn-outline-success px-3 rounded-pill fw-bold" @click="triggerCSVExport" title="Export medical history to CSV via background batch job">
                            <i class="bi bi-file-earmark-spreadsheet me-1"></i>Download Records (CSV)
                        </button>
                        <button class="btn btn-sm btn-outline-primary px-3 rounded-pill fw-bold" @click="exportData">
                            <i class="bi bi-file-pdf me-1"></i>Export PDF Report
                        </button>
                    </div>
                </div>

                <!-- Next Upcoming Appointment Alert Banner -->
                <div v-if="nextUpcomingAppointment" class="alert alert-primary border-0 shadow-sm p-4 mb-4 rounded-4 d-flex align-items-center justify-content-between fade-in-up" style="background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%); border-left: 6px solid #0284c7 !important;">
                    <div class="d-flex align-items-center gap-3">
                        <div class="bg-primary text-white rounded-circle d-flex align-items-center justify-content-center" style="width: 48px; height: 48px;">
                            <i class="bi bi-calendar-check-fill fs-4"></i>
                        </div>
                        <div>
                            <span class="text-primary fw-bold text-uppercase small tracking-wider d-block mb-1">Next Upcoming Appointment</span>
                            <h5 class="fw-extrabold text-dark mb-0">
                                Dr. {{ nextUpcomingAppointment.doctor_name }} on {{ nextUpcomingAppointment.date }} @ {{ nextUpcomingAppointment.time_slot }}
                            </h5>
                        </div>
                    </div>
                    <span class="badge bg-primary text-white px-3 py-2 rounded-pill fw-bold text-uppercase fs-6">Booked</span>
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

        <!-- Checkout Overlay Modal -->
        <transition name="fade">
            <div v-if="showCheckout" class="reschedule-overlay d-flex align-items-center justify-content-center">
                <div class="card border-0 shadow-lg p-2 reschedule-card rounded-4 bg-pastel-blue">
                    <div class="card-header bg-transparent border-0 pt-4 pb-2 d-flex justify-content-between align-items-center">
                        <h5 class="mb-0 fw-bold text-dark"><i class="bi bi-credit-card-2-front me-2"></i>Consultation Checkout</h5>
                        <button type="button" class="btn-close" @click="closeCheckout"></button>
                    </div>
                    <div class="card-body">
                        <div class="checkout-summary bg-light rounded-3 p-3 mb-4 border border-dashed border-secondary">
                            <div class="d-flex justify-content-between mb-2">
                                <span class="text-muted small">Provider</span>
                                <strong class="text-dark">{{ checkoutData.doctor_name }}</strong>
                            </div>
                            <div class="d-flex justify-content-between mb-2">
                                <span class="text-muted small">Specialty</span>
                                <span class="badge bg-secondary font-heading rounded-pill">{{ checkoutData.specialization }}</span>
                            </div>
                            <div class="d-flex justify-content-between mb-2">
                                <span class="text-muted small">Date & Time</span>
                                <strong class="text-dark">{{ bookForm.date }} @ {{ bookForm.time_slot }}</strong>
                            </div>
                            <hr class="my-2">
                            <div class="d-flex justify-content-between align-items-center">
                                <span class="fw-bold text-dark">Consultation Fee</span>
                                <h4 class="text-primary fw-extrabold mb-0">₹{{ checkoutData.amount ? checkoutData.amount.toFixed(2) : '50.00' }}</h4>
                            </div>
                        </div>

                        <form @submit.prevent="processPayment" class="d-flex flex-column gap-3">
                            <div>
                                <label class="form-label text-secondary small fw-bold">Cardholder Name</label>
                                <div class="input-icon-wrapper">
                                    <input type="text" class="form-control" v-model="cardForm.cardholder" placeholder="John Doe" required>
                                </div>
                            </div>
                            <div>
                                <label class="form-label text-secondary small fw-bold">Card Number</label>
                                <div class="input-icon-wrapper">
                                    <input type="text" class="form-control" v-model="cardForm.number" placeholder="1234567812345678" pattern="\d{16}" title="16-digit card number" required>
                                </div>
                            </div>
                            <div class="row g-2">
                                <div class="col-6">
                                    <label class="form-label text-secondary small fw-bold">Expiry Date</label>
                                    <input type="text" class="form-control" v-model="cardForm.expiry" placeholder="MM/YY" pattern="(0[1-9]|1[0-2])\/\d{2}" title="MM/YY format" required>
                                </div>
                                <div class="col-6">
                                    <label class="form-label text-secondary small fw-bold">CVV</label>
                                    <input type="password" class="form-control" v-model="cardForm.cvv" placeholder="•••" pattern="\d{3,4}" title="3 or 4 digit CVV" required>
                                </div>
                            </div>

                            <button type="submit" class="btn btn-primary w-100 py-3 text-white fw-bold mt-3 shadow" :disabled="paymentProcessing">
                                <span v-if="paymentProcessing" class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
                                <span v-if="paymentProcessing">Authorizing Transaction...</span>
                                <span v-else><i class="bi bi-lock-fill me-1"></i>Pay & Confirm Booking</span>
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </transition>

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

        <!-- Floating Theme Toggle (Light/Dark Mode only) -->
        <button class="theme-customizer-trigger" @click="toggleDarkMode" :title="isDarkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode'">
            <i class="bi" :class="isDarkMode ? 'bi-sun-fill text-warning' : 'bi-moon-fill text-white'"></i>
        </button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            token: localStorage.getItem('access_token'),
            patientName: localStorage.getItem('username') || 'Patient',
            error: '', success: '',
            searchQuery: '', searchResults: [], targetDoctor: null, departments: [],
            bookForm: { date: '', time_slot: '' },
            profileForm: { contact: '', address: '' },
            history: [],
            rescheduleData: null, rescheduleForm: { date: '', time_slot: '' },
            currentTab: 'booking',
            isDarkMode: false,
            showCheckout: false,
            checkoutData: { amount: 0, doctor_name: '', specialization: '', appointment_id: null, order_id: '' },
            cardForm: { cardholder: '', number: '', expiry: '', cvv: '' },
            paymentProcessing: false
        }
    },
    computed: {
        nextUpcomingAppointment() {
            if (!this.history || this.history.length === 0) return null;
            const todayStr = new Date().toISOString().split('T')[0];
            const upcoming = this.history.filter(h => h.status === 'Booked' && h.date >= todayStr);
            if (upcoming.length === 0) return null;
            
            upcoming.sort((a, b) => {
                const dateCompare = a.date.localeCompare(b.date);
                if (dateCompare !== 0) return dateCompare;
                return a.time_slot.localeCompare(b.time_slot);
            });
            return upcoming[0];
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
            try {
                const res = await fetch('http://127.0.0.1:5000/api/payments/create-order', {
                    method: 'POST', headers: this.authHeader(), body: JSON.stringify(payload)
                });
                const data = await res.json();
                if (res.ok) {
                    this.checkoutData = data;
                    this.showCheckout = true;
                    this.cardForm = { cardholder: '', number: '', expiry: '', cvv: '' };
                } else {
                    this.showMsg('error', data.message);
                }
            } catch {
                this.showMsg('error', "Failed to initialize checkout.");
            }
        },
        closeCheckout() {
            this.showCheckout = false;
            this.checkoutData = { amount: 0, doctor_name: '', specialization: '', appointment_id: null, order_id: '' };
        },
        async processPayment() {
            this.paymentProcessing = true;
            await new Promise(resolve => setTimeout(resolve, 1500));
            try {
                const transactionId = 'MOCK-TXN-' + Math.random().toString(36).substr(2, 9).toUpperCase();
                const payload = {
                    appointment_id: this.checkoutData.appointment_id,
                    order_id: this.checkoutData.order_id,
                    transaction_id: transactionId,
                    cardholder_name: this.cardForm.cardholder
                };
                const res = await fetch('http://127.0.0.1:5000/api/payments/verify', {
                    method: 'POST', headers: this.authHeader(), body: JSON.stringify(payload)
                });
                const data = await res.json();
                this.paymentProcessing = false;
                if (res.ok) {
                    this.showMsg('success', "Payment Successful! Appointment confirmed.");
                    this.showCheckout = false;
                    this.targetDoctor = null;
                    this.bookForm = { date: '', time_slot: '' };
                    this.fetchHistory();
                } else {
                    this.showMsg('error', data.message);
                }
            } catch {
                this.paymentProcessing = false;
                this.showMsg('error', "Payment verification failed.");
            }
        },
        async exportData() {
            const res = await fetch('http://127.0.0.1:5000/api/patient/export-history', { method: 'POST', headers: this.authHeader() });
            if (res.ok) {
                const blob = await res.blob();
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'Medical_History_Report.pdf';
                document.body.appendChild(a);
                a.click();
                a.remove();
                this.showMsg('success', "Medical Record PDF downloaded!");
            } else {
                this.showMsg('error', "Failed to download medical report PDF.");
            }
        },
        async triggerCSVExport() {
            try {
                const res = await fetch('http://127.0.0.1:5000/api/patient/export-csv', { method: 'POST', headers: this.authHeader() });
                const data = await res.json();
                if (res.ok) {
                    this.showMsg('success', data.message);
                } else {
                    this.showMsg('error', data.message || "Failed to trigger CSV export.");
                }
            } catch (e) {
                this.showMsg('error', "Network error triggering CSV export.");
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
        },
        toggleDarkMode() {
            this.isDarkMode = !this.isDarkMode;
            localStorage.setItem('theme-dark', this.isDarkMode);
            if (this.isDarkMode) {
                document.body.classList.add('dark-theme');
            } else {
                document.body.classList.remove('dark-theme');
            }
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

/* Padding left removed for plain inputs */

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
