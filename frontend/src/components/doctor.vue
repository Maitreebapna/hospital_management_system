<template>
    <div class="dashboard-container fade-in-up">
        <!-- Modern Left Sidebar Navigation -->
        <div class="dashboard-sidebar text-white">
            <div>
                <!-- Brand logo area -->
                <div class="sidebar-brand">
                    <div>
                        <span class="fw-bold tracking-tight text-white fs-4 d-block">HMS Doctor</span>
                        <span class="text-muted small" style="font-size: 11px !important;">Provider Portal</span>
                    </div>
                </div>
                
                <!-- Menu Links -->
                <div class="sidebar-nav-menu">
                    <button class="sidebar-nav-btn" :class="{active: currentTab === 'appointments'}" @click="currentTab = 'appointments'">
                        <i class="bi bi-journal-check"></i>
                        <span>Appointments</span>
                    </button>
                    <button class="sidebar-nav-btn" :class="{active: currentTab === 'schedule'}" @click="currentTab = 'schedule'">
                        <i class="bi bi-calendar-week"></i>
                        <span>My Schedule</span>
                    </button>
                    <button class="sidebar-nav-btn" :class="{active: currentTab === 'patients'}" @click="currentTab = 'patients'">
                        <i class="bi bi-people-fill"></i>
                        <span>My Patients</span>
                    </button>
                </div>
            </div>
            
            <!-- User Profile & Logout at Bottom -->
            <div class="sidebar-footer-profile">
                <div class="d-flex align-items-center gap-2">
                    <div class="sidebar-avatar">{{ doctorName ? doctorName.charAt(0) : 'D' }}</div>
                    <div>
                        <span class="text-white fw-bold d-block small text-truncate" style="max-width: 110px;">{{ doctorName }}</span>
                        <span class="text-muted small d-block" style="font-size: 10px !important; max-width: 110px;">{{ specialization }} Dept</span>
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
                 TAB 1: APPOINTMENTS
            ------------------------------------------ -->
            <div v-show="currentTab === 'appointments'" class="fade-in-up">
                <div class="d-flex justify-content-between align-items-center mb-4">
                    <h3 class="mb-0 fw-bold font-heading text-primary">Patient Visit Records</h3>
                    <span class="text-muted small fw-medium">Real-time update</span>
                </div>

                <div class="row g-4">
                    <!-- Upcoming Weekly Schedule Timeline -->
                    <div class="col-12">
                        <div class="card shadow-sm border-0">
                            <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
                                <i class="bi bi-calendar-check text-primary fs-5"></i>
                                <h5 class="mb-0 fw-bold text-dark">Upcoming Weekly Schedule</h5>
                            </div>
                            <div class="card-body p-4 bg-white">
                                <!-- Timeline Layout -->
                                <div class="timeline-container" v-if="appointments.length > 0">
                                    <div class="timeline-item position-relative ps-5 pb-4" v-for="appt in appointments" :key="appt.id">
                                        <!-- Timeline node clock icon -->
                                        <div class="timeline-badge bg-primary text-white position-absolute rounded-circle d-flex align-items-center justify-content-center shadow-sm" style="left: 12px; top: 0; width: 34px; height: 34px; z-index: 2;">
                                            <i class="bi bi-clock-fill fs-6"></i>
                                        </div>
                                        
                                        <!-- Card style layout for timeline item -->
                                        <div class="card border-0 shadow-sm bg-light-subtle rounded-3 p-3 timeline-card">
                                            <div class="d-flex flex-column flex-md-row align-items-md-center justify-content-between gap-3">
                                                <div>
                                                    <!-- Time Slot & Date -->
                                                    <div class="d-flex align-items-center gap-2 mb-2">
                                                        <span class="badge bg-primary rounded-pill px-3 py-1.5 fw-bold fs-6">
                                                            {{ appt.time_slot }}
                                                        </span>
                                                        <span class="text-muted fw-semibold small">
                                                            <i class="bi bi-calendar3 me-1"></i>{{ appt.date }}
                                                        </span>
                                                    </div>
                                                    
                                                    <!-- Patient Info -->
                                                    <div class="d-flex align-items-center gap-2">
                                                        <div class="bg-primary-subtle text-primary rounded-circle d-flex align-items-center justify-content-center" style="width: 32px; height: 32px;">
                                                            <i class="bi bi-person-fill"></i>
                                                        </div>
                                                        <div>
                                                            <h6 class="mb-0 fw-extrabold text-dark">{{ appt.patient_name }}</h6>
                                                            <span class="text-muted small">Appointment ID: #{{ appt.id }}</span>
                                                        </div>
                                                    </div>
                                                </div>
                                                
                                                <!-- Status & Actions -->
                                                <div class="d-flex align-items-center gap-3">
                                                    <span class="badge rounded-pill px-3 py-2 text-uppercase fw-bold" :class="{'bg-success-subtle text-success border border-success-subtle': appt.status === 'Completed', 'bg-warning-subtle text-warning-emphasis border border-warning-subtle': appt.status === 'Cancelled', 'bg-primary-subtle text-primary border border-primary-subtle': appt.status === 'Booked'}">
                                                        {{ appt.status }}
                                                    </span>
                                                    
                                                    <div v-if="appt.status === 'Booked'" class="d-flex gap-2">
                                                        <button class="btn btn-sm btn-primary px-3 py-2 fw-bold shadow-sm rounded-pill" @click="openTreatmentModal(appt)">
                                                            <i class="bi bi-journal-medical me-1"></i>Add Treatment
                                                        </button>
                                                        <button class="btn btn-sm btn-outline-danger px-3 py-2 fw-bold rounded-pill" @click="cancelAppt(appt.id)" title="Cancel Appointment">
                                                            <i class="bi bi-x-circle me-1"></i>Cancel
                                                        </button>
                                                    </div>
                                                    <span v-else class="text-muted small italic">Handled</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="text-center text-muted py-5" v-else>
                                    <i class="bi bi-calendar-x fs-2 d-block mb-2"></i>
                                    No upcoming appointments found.
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- -----------------------------------------
                 TAB 2: SCHEDULE CONFIG
            ------------------------------------------ -->
            <div v-show="currentTab === 'schedule'" class="fade-in-up">
                <div class="d-flex justify-content-between align-items-center mb-4">
                    <h3 class="mb-0 fw-bold font-heading text-primary">Manage Schedule</h3>
                </div>

                <div class="row g-4">
                    <div class="col-md-6">
                        <div class="card shadow-sm border-0 h-100">
                            <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
                                <i class="bi bi-calendar-range text-primary fs-5"></i>
                                <h5 class="mb-0 fw-bold text-dark">Active Hours Details</h5>
                            </div>
                            <div class="card-body p-4 bg-white d-flex flex-column justify-content-between">
                                <div class="schedule-display bg-light rounded-3 p-4 mb-4">
                                    <div class="d-flex align-items-center gap-3 mb-4">
                                        <div class="bg-primary text-white rounded-circle p-2 d-flex align-items-center justify-content-center" style="width: 44px; height: 44px;">
                                            <i class="bi bi-calendar-day fs-5"></i>
                                        </div>
                                        <div>
                                            <span class="text-muted small d-block">Configured Days</span>
                                            <h5 class="text-dark mb-0 fw-bold">{{ availability || 'Not Set' }}</h5>
                                        </div>
                                    </div>
                                    <div class="d-flex align-items-center gap-3">
                                        <div class="bg-primary text-white rounded-circle p-2 d-flex align-items-center justify-content-center" style="width: 44px; height: 44px;">
                                            <i class="bi bi-clock fs-5"></i>
                                        </div>
                                        <div>
                                            <span class="text-muted small d-block">Configured Hours</span>
                                            <h5 class="text-dark mb-0 fw-bold">{{ time_availability || 'Not Set' }}</h5>
                                        </div>
                                    </div>
                                </div>
                                <span class="text-muted small"><i class="bi bi-info-circle me-1"></i>These availability settings will be displayed to patients during appointment bookings.</span>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-6">
                        <div class="card shadow-sm border-0">
                            <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
                                <i class="bi bi-pencil-square text-primary fs-5"></i>
                                <h5 class="mb-0 fw-bold text-dark">Update Working Hours</h5>
                            </div>
                            <div class="card-body p-4 bg-white">
                                <form @submit.prevent="updateAvailability" class="d-flex flex-column gap-3">
                                    <div>
                                        <label class="form-label text-secondary small fw-bold">Select Day(s)</label>
                                        <select class="form-select" v-model="availability" required>
                                            <option value="" disabled>Select Day</option>
                                            <option value="Monday">Monday</option>
                                            <option value="Tuesday">Tuesday</option>
                                            <option value="Wednesday">Wednesday</option>
                                            <option value="Thursday">Thursday</option>
                                            <option value="Friday">Friday</option>
                                            <option value="Saturday">Saturday</option>
                                            <option value="Sunday">Sunday</option>
                                            <option value="Everyday">Everyday</option>
                                        </select>
                                    </div>
                                    <div>
                                        <label class="form-label text-secondary small fw-bold">Working Hours Range</label>
                                        <div class="input-icon-wrapper">
                                            <input type="text" class="form-control" v-model="time_availability" placeholder="e.g. 10:00 AM - 05:00 PM" required>
                                        </div>
                                    </div>
                                    <button class="btn btn-primary w-100 py-3 rounded-3 mt-2 shadow-sm fw-bold">
                                        <i class="bi bi-arrow-repeat me-1"></i>Update Active Schedule
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- -----------------------------------------
                 TAB 3: MY PATIENTS & CLINICAL HISTORY
            ------------------------------------------ -->
            <div v-show="currentTab === 'patients'" class="fade-in-up">
                <div class="d-flex justify-content-between align-items-center mb-4">
                    <h3 class="mb-0 fw-bold font-heading text-primary">Assigned Patients & History</h3>
                </div>

                <div class="row g-4">
                    <!-- Patients list -->
                    <div class="col-md-5">
                        <div class="card shadow-sm border-0">
                            <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
                                <i class="bi bi-people-fill text-primary fs-5"></i>
                                <h5 class="mb-0 fw-bold text-dark">Registered Patients</h5>
                            </div>
                            <div class="card-body p-3 bg-white">
                                <div class="patients-list-scroll pe-1" style="max-height: 500px; overflow-y: auto;" v-if="patients.length > 0">
                                    <div class="patient-item d-flex justify-content-between align-items-center p-3 mb-2 rounded-3 border bg-light transition-all" v-for="pat in patients" :key="pat.patient_id">
                                        <div class="d-flex align-items-center gap-2" style="min-width: 0;">
                                            <div class="bg-primary-light text-primary rounded-circle d-flex align-items-center justify-content-center" style="width: 38px; height: 38px; flex-shrink: 0;">
                                                <i class="bi bi-person-fill"></i>
                                            </div>
                                            <div style="min-width: 0;">
                                                <strong class="text-dark d-block text-truncate">{{ pat.name }}</strong>
                                                <span class="text-muted small text-truncate d-block"><i class="bi bi-telephone me-1"></i>{{ pat.contact }}</span>
                                            </div>
                                        </div>
                                        <button class="btn btn-sm btn-outline-primary px-3 rounded-pill" @click="viewPatientHistory(pat)">
                                            <i class="bi bi-file-earmark-text me-1"></i>History
                                        </button>
                                    </div>
                                </div>
                                <div v-else class="text-center text-muted py-5">
                                    <i class="bi bi-people fs-2 d-block mb-2"></i>
                                    No patients registered yet.
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Medical history timeline -->
                    <div class="col-md-7">
                        <transition name="fade">
                            <div class="card border-0 shadow-sm" v-if="selectedPatient">
                                <div class="card-header bg-white py-3 border-bottom d-flex justify-content-between align-items-center">
                                    <div class="d-flex align-items-center gap-2">
                                        <i class="bi bi-clock-history text-primary fs-5"></i>
                                        <h5 class="mb-0 fw-bold text-dark">Prescription: {{ selectedPatient.name }}</h5>
                                    </div>
                                    <button type="button" class="btn-close" @click="selectedPatient = null"></button>
                                </div>
                                <div class="card-body bg-light p-4">
                                    <div class="timeline-container d-flex flex-column gap-3">
                                        <div class="timeline-item bg-white p-3 rounded-3 shadow-sm border" v-for="h in patientHistory" :key="h.id">
                                            <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center border-bottom pb-2 mb-2 gap-2">
                                                <div class="d-flex align-items-center gap-2">
                                                    <i class="bi bi-calendar3 text-muted"></i>
                                                    <span class="fw-bold text-dark">{{ h.date }}</span>
                                                    <span class="badge bg-secondary rounded-pill">{{ h.time_slot }}</span>
                                                </div>
                                                <span class="badge rounded-pill align-self-start align-self-md-auto" :class="{'bg-success-subtle text-success': h.status === 'Completed', 'bg-warning-subtle text-warning-emphasis': h.status === 'Cancelled', 'bg-primary-subtle text-primary': h.status === 'Booked'}">
                                                    {{ h.status }}
                                                </span>
                                            </div>
                                            
                                            <div v-if="h.treatment" class="treatment-box p-3 rounded bg-light border-start border-primary border-4">
                                                <div class="mb-2"><strong class="text-primary small text-uppercase">Diagnosis:</strong> <div class="text-dark fw-medium mt-1">{{ h.treatment.diagnosis }}</div></div>
                                                <div class="mb-2"><strong class="text-primary small text-uppercase">Prescription:</strong> <div class="text-dark fw-medium mt-1">{{ h.treatment.prescription }}</div></div>
                                                <div v-if="h.treatment.notes"><strong class="text-primary small text-uppercase">Clinical Notes:</strong> <div class="text-muted small mt-1">{{ h.treatment.notes }}</div></div>
                                            </div>
                                            
                                            <button v-if="h.treatment || h.status === 'Completed'"
                                                class="btn btn-sm btn-outline-warning mt-3 text-dark fw-bold" @click="editHistory(h)">
                                                <i class="bi bi-pencil-square me-1"></i>Edit Notes / Diagnosis
                                            </button>
                                        </div>
                                        <div v-if="patientHistory.length === 0" class="text-center text-muted py-4">
                                            No historical records found for this patient.
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div v-else class="card border-0 shadow-sm h-100">
                                <div class="card-body d-flex flex-column align-items-center justify-content-center p-5 text-muted text-center">
                                    <i class="bi bi-file-earmark-person display-4 mb-3 text-muted"></i>
                                    <h5>Patient Selection Required</h5>
                                    <p class="small mb-0">Click the "History" button beside any patient on the left to view their clinical medical logs.</p>
                                </div>
                            </div>
                        </transition>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Floating Theme Toggle (Light/Dark Mode only) -->
        <button class="theme-customizer-trigger" @click="toggleDarkMode" :title="isDarkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode'">
            <i class="bi" :class="isDarkMode ? 'bi-sun-fill text-warning' : 'bi-moon-fill text-white'"></i>
        </button>

        <!-- Bootstrap 5 Styled Treatment Modal -->
        <div class="modal fade show d-block" style="background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(4px); z-index: 1060;" v-if="showTreatmentModal">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content border-0 shadow-lg rounded-4 overflow-hidden animate-zoom">
                    <div class="modal-header bg-teal text-white border-0 py-3">
                        <h5 class="modal-title fw-bold mb-0"><i class="bi bi-file-earmark-medical me-2"></i>Add Treatment: {{ activePatientName }}</h5>
                        <button type="button" class="btn-close btn-close-white" @click="closeTreatmentModal"></button>
                    </div>
                    <form @submit.prevent="saveTreatment">
                        <div class="modal-body p-4 bg-white">
                            <div class="d-flex flex-column gap-3">
                                <div>
                                    <label class="form-label text-secondary small fw-bold">Medical Diagnosis</label>
                                    <input type="text" class="form-control" v-model="treatment.diagnosis" required>
                                </div>
                                <div>
                                    <label class="form-label text-secondary small fw-bold">Prescribed Medication</label>
                                    <input type="text" class="form-control" v-model="treatment.prescription" required>
                                </div>
                                <div>
                                    <label class="form-label text-secondary small fw-bold">Clinical Notes</label>
                                    <textarea class="form-control" v-model="treatment.notes" rows="3"></textarea>
                                </div>
                            </div>
                        </div>
                        <div class="modal-footer bg-light border-0 py-3">
                            <button type="button" class="btn btn-outline-secondary rounded-pill px-4" @click="closeTreatmentModal">Cancel</button>
                            <button type="submit" class="btn btn-success rounded-pill px-4 fw-bold">
                                <i class="bi bi-file-earmark-check me-2"></i>Save & Complete
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            token: localStorage.getItem('access_token'),
            error: '', success: '', availability: '', time_availability: '',
            doctorName: '', specialization: '',
            appointments: [], activeApptId: null, activePatientName: '',
            treatment: { diagnosis: '', prescription: '', notes: '' },
            patients: [], selectedPatient: null, patientHistory: [],
            currentTab: 'appointments',
            isDarkMode: false,
            showTreatmentModal: false
        }
    },
    methods: {
        authHeader() { return { 'Authorization': 'Bearer ' + this.token, 'Content-Type': 'application/json' }; },
        logout() { localStorage.clear(); window.location.href = '/index.html'; },
        showMsg(type, msg) {
            if (type === 'success') {
                this.success = msg;
                setTimeout(() => { if (this.success === msg) this.success = ''; }, 5000);
            } else {
                this.error = msg;
                setTimeout(() => { if (this.error === msg) this.error = ''; }, 5000);
            }
        },
        async fetchData() {
            const res = await fetch('http://127.0.0.1:5000/api/doctor/dashboard', { headers: this.authHeader() });
            if (res.ok) this.appointments = await res.json();
            
            const res2 = await fetch('http://127.0.0.1:5000/api/doctor/profile', { headers: this.authHeader() });
            if (res2.ok) {
                const profile = await res2.json();
                this.doctorName = profile.name;
                this.specialization = profile.specialization;
                this.availability = profile.availability;
                this.time_availability = profile.time_availability;
            }
            this.fetchPatients();
        },
        async updateAvailability() {
            const res = await fetch('http://127.0.0.1:5000/api/doctor/availability', {
                method: 'PUT', headers: this.authHeader(), body: JSON.stringify({ 
                    availability: this.availability,
                    time_availability: this.time_availability 
                })
            });
            if (res.ok) { this.showMsg('success', "Your schedule is now updated."); }
        },
        openTreatmentModal(appt) {
            this.activeApptId = appt.id;
            this.activePatientName = appt.patient_name;
            this.treatment = { diagnosis: '', prescription: '', notes: '' };
            this.showTreatmentModal = true;
            this.success = '';
        },
        closeTreatmentModal() {
            this.showTreatmentModal = false;
            this.activeApptId = null;
        },
        async saveTreatment() {
            const payload = { appointment_id: this.activeApptId, ...this.treatment };
            const res = await fetch('http://127.0.0.1:5000/api/doctor/treatment', {
                method: 'POST', headers: this.authHeader(), body: JSON.stringify(payload)
            });
            if (res.ok) {
                this.showMsg('success', "Medical record saved.");
                this.activeApptId = null;
                this.treatment = { diagnosis: '', prescription: '', notes: '' };
                this.showTreatmentModal = false;
                this.fetchData();
                if (this.selectedPatient) this.viewPatientHistory(this.selectedPatient);
            } else {
                const data = await res.json();
                this.showMsg('error', data.message);
            }
        },
        async fetchPatients() {
            const res = await fetch('http://127.0.0.1:5000/api/doctor/patients', { headers: this.authHeader() });
            if (res.ok) this.patients = await res.json();
        },
        async cancelAppt(id) {
            if (confirm("Are you sure you want to cancel this appointment?")) {
                const res = await fetch('http://127.0.0.1:5000/api/doctor/appointment/' + id, {
                    method: 'PATCH', headers: this.authHeader(), body: JSON.stringify({ status: 'Cancelled' })
                });
                if (res.ok) { this.showMsg('success', "Appointment cancelled"); this.fetchData(); }
                else { const data = await res.json(); this.showMsg('error', data.message); }
            }
        },
        async viewPatientHistory(pat) {
            this.selectedPatient = pat;
            const res = await fetch('http://127.0.0.1:5000/api/patient/' + pat.patient_id + '/history', { headers: this.authHeader() });
            if (res.ok) {
                const data = await res.json();
                this.patientHistory = data.history;
            }
        },
        editHistory(h) {
            this.activeApptId = h.id;
            this.activePatientName = this.selectedPatient ? this.selectedPatient.name : 'Unknown';
            this.treatment = {
                diagnosis: h.treatment ? h.treatment.diagnosis : '',
                prescription: h.treatment ? h.treatment.prescription : '',
                notes: h.treatment ? h.treatment.notes : ''
            };
            this.showTreatmentModal = true;
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
        if (!this.token || localStorage.getItem('role') !== 'Doctor') this.logout();
        else this.fetchData();
    }
}
</script>

<style scoped>
.doctor-dashboard-wrapper {
    min-height: 100vh;
    background-color: #f8fafc;
}

.nav-brand-icon {
    background: linear-gradient(135deg, #0d9488 0%, #0f766e 100%) !important;
}

.bg-primary-light {
    background-color: rgba(13, 148, 136, 0.1) !important;
    color: #0d9488 !important;
}

.patient-item {
    transition: var(--transition-smooth);
}

.patient-item:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02);
    border-color: #0d9488 !important;
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
    border-left: 4px solid #0d9488 !important;
}

.patients-list-scroll::-webkit-scrollbar {
    width: 6px;
}
.patients-list-scroll::-webkit-scrollbar-track {
    background: transparent;
}
.patients-list-scroll::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 10px;
}

/* Vertical Schedule Timeline */
.timeline-container {
    position: relative;
}

.timeline-container::before {
    content: '';
    position: absolute;
    top: 15px;
    bottom: 15px;
    left: 28px;
    width: 2px;
    background-color: #e2e8f0;
    z-index: 1;
}

.timeline-item:last-child {
    padding-bottom: 0 !important;
}

.timeline-card {
    transition: all 0.3s ease;
    border-left: 4px solid #0d9488 !important;
}

.timeline-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.05) !important;
}

.bg-teal {
    background-color: #0d9488 !important;
}

/* Animations */
.slide-up-enter-active, .slide-up-leave-active { transition: all 0.3s ease; }
.slide-up-enter-from, .slide-up-leave-to { opacity: 0; transform: translateY(10px); }
.fade-enter-active, .fade-leave-active { transition: opacity 0.3s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

@keyframes zoomIn {
    from { opacity: 0; transform: scale(0.95); }
    to { opacity: 1; transform: scale(1); }
}

.animate-zoom {
    animation: zoomIn 0.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
</style>
