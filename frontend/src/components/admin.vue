<template>
    <div class="dashboard-container fade-in-up">
        <!-- Modern Left Sidebar Navigation -->
        <div class="dashboard-sidebar text-white">
            <div>
                <!-- Brand logo area -->
                <div class="sidebar-brand">
                    <div>
                        <span class="fw-bold tracking-tight text-white fs-4 d-block">HMS</span>
                        <span class="text-muted small" style="font-size: 11px !important;">Administration Portal</span>
                    </div>
                </div>
                
                <!-- Menu Links -->
                <div class="sidebar-nav-menu">
                    <button class="sidebar-nav-btn" :class="{active: currentTab === 'overview'}" @click="currentTab = 'overview'">
                        <i class="bi bi-grid-1x2-fill"></i>
                        <span>Overview</span>
                    </button>
                    <button class="sidebar-nav-btn" :class="{active: currentTab === 'doctors'}" @click="currentTab = 'doctors'">
                        <i class="bi bi-person-badge-fill"></i>
                        <span>Manage Doctors</span>
                    </button>
                    <button class="sidebar-nav-btn" :class="{active: currentTab === 'patients'}" @click="currentTab = 'patients'">
                        <i class="bi bi-people-fill"></i>
                        <span>Manage Patients</span>
                    </button>
                </div>
            </div>
            
            <!-- User Profile & Logout at Bottom -->
            <div class="sidebar-footer-profile">
                <div class="d-flex align-items-center gap-2">
                    <div class="sidebar-avatar">A</div>
                    <div>
                        <span class="text-white fw-bold d-block small">Admin</span>
                        <span class="text-muted small d-block" style="font-size: 10px !important;"></span>
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
                <div v-if="error" class="alert alert-danger shadow-sm border-0 mb-4">
                    <i class="bi bi-exclamation-triangle-fill fs-5"></i>
                    <div>{{ error }}</div>
                </div>
            </transition>
            <transition name="fade">
                <div v-if="success" class="alert alert-success shadow-sm border-0 mb-4">
                    <i class="bi bi-check-circle-fill fs-5"></i>
                    <div>{{ success }}</div>
                </div>
            </transition>

            <!-- -----------------------------------------
                 TAB 1: OVERVIEW & STATS
            ------------------------------------------ -->
            <div v-show="currentTab === 'overview'" class="fade-in-up">
                <div class="d-flex justify-content-between align-items-center mb-4">
                    <h3 class="mb-0 fw-bold font-heading text-primary-blue">Hospital Administration Overview</h3>
                    <span class="text-muted small fw-medium"></span>
                </div>
                
                <!-- Stats Cards Section -->
                <div class="row g-4 mb-5">
                    <div class="col-md-4">
                        <div class="card stat-card stat-card-interactive shadow-sm border-0 h-100" @click="currentTab = 'patients'">
                            <div class="card-body d-flex align-items-center justify-content-between p-4 bg-white">
                                <div>
                                    <span class="text-muted small fw-bold text-uppercase tracking-wider">Total Patients</span>
                                    <h2 class="display-6 fw-extrabold text-dark mt-2 mb-0">{{ stats.total_patients }}</h2>
                                </div>
                                <div class="stat-icon-container bg-primary-light text-primary">
                                    <i class="bi bi-people-fill fs-3"></i>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card stat-card stat-card-interactive shadow-sm border-0 h-100" @click="currentTab = 'doctors'">
                            <div class="card-body d-flex align-items-center justify-content-between p-4 bg-white">
                                <div>
                                    <span class="text-muted small fw-bold text-uppercase tracking-wider">Total Doctors</span>
                                    <h2 class="display-6 fw-extrabold text-dark mt-2 mb-0">{{ stats.total_doctors }}</h2>
                                </div>
                                <div class="stat-icon-container bg-primary-light text-primary">
                                    <i class="bi bi-person-badge-fill fs-3"></i>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card stat-card shadow-sm border-0 h-100">
                            <div class="card-body d-flex align-items-center justify-content-between p-4 bg-white">
                                <div>
                                    <span class="text-muted small fw-bold text-uppercase tracking-wider">Total Appointments</span>
                                    <h2 class="display-6 fw-extrabold text-dark mt-2 mb-0">{{ stats.total_appointments }}</h2>
                                </div>
                                <div class="stat-icon-container bg-primary-light text-primary">
                                    <i class="bi bi-calendar-check-fill fs-3"></i>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Appointments and Graphical Analytics Row -->
                <div class="row g-4">
                    <!-- Appointments Table (Left) -->
                    <div class="col-xl-8">
                        <div class="card shadow-sm border-0 h-100">
                            <div class="card-header bg-white py-3 border-bottom d-flex flex-column flex-sm-row justify-content-between align-items-sm-center gap-3">
                                <div class="d-flex align-items-center gap-2">
                                    <i class="bi bi-calendar-range text-primary fs-5"></i>
                                    <h5 class="mb-0 fw-bold text-dark">Appointment Records</h5>
                                </div>
                                <div class="d-flex gap-3 align-items-center justify-content-between">
                                    <label class="mb-0 fw-bold small text-muted text-nowrap">Filter Status:</label>
                                    <select class="form-select form-select-sm border-1 shadow-sm w-auto bg-light" v-model="appointmentFilter">
                                        <option value="All">All Status</option>
                                        <option value="Booked">Booked</option>
                                        <option value="Completed">Completed</option>
                                        <option value="Cancelled">Cancelled</option>
                                    </select>
                                </div>
                            </div>
                            <div class="card-body p-0 bg-white">
                                <div class="table-responsive border-0">
                                    <table class="table table-hover table-striped mb-0">
                                        <thead>
                                            <tr>
                                                <th style="width: 80px;">ID</th>
                                                <th>Doctor Name</th>
                                                <th>Patient Name</th>
                                                <th>Appointment Date</th>
                                                <th>Time Slot</th>
                                                <th>Status</th>
                                                <th class="text-end">Actions</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="appt in filteredAppointments" :key="appt.id" class="align-middle">
                                                <td class="fw-bold text-muted">#{{ appt.id }}</td>
                                                <td>
                                                    <div class="d-flex align-items-center gap-2">
                                                        <div class="bg-light text-primary rounded-circle d-flex align-items-center justify-content-center" style="width: 28px; height: 28px;">
                                                            <i class="bi bi-person-fill"></i>
                                                        </div>
                                                        <div>
                                                            <strong class="text-dark d-block">{{ appt.doctor }}</strong>
                                                            <small class="text-muted" style="font-size: 11px !important; font-weight: 500;">
                                                                <i class="bi bi-patch-check-fill text-primary me-1"></i>{{ getDocSpecialization(appt.doctor) }}
                                                            </small>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>{{ appt.patient }}</td>
                                                <td>
                                                    <div class="d-flex align-items-center gap-2">
                                                        <i class="bi bi-calendar3 text-muted small"></i>
                                                        <span>{{ appt.date }}</span>
                                                    </div>
                                                </td>
                                                <td>
                                                    <span class="badge bg-secondary rounded-pill px-3 py-2">{{ appt.time_slot }}</span>
                                                </td>
                                                <td>
                                                    <span class="badge rounded-pill px-3 py-2" :class="{'bg-success-subtle text-success border border-success-subtle': appt.status === 'Completed', 'bg-warning-subtle text-warning-emphasis border border-warning-subtle': appt.status === 'Cancelled', 'bg-primary-subtle text-primary border border-primary-subtle': appt.status === 'Booked'}">
                                                        <i class="bi" :class="{'bi-check-circle-fill': appt.status === 'Completed', 'bi-x-circle-fill': appt.status === 'Cancelled', 'bi-clock-fill': appt.status === 'Booked'}"></i>
                                                        {{ appt.status }}
                                                    </span>
                                                </td>
                                                <td class="text-end">
                                                    <div class="d-flex justify-content-end gap-2">
                                                        <button v-if="appt.status !== 'Cancelled'" class="btn-action-circle warning"
                                                            @click="updateAppointmentStatus(appt.id, 'Cancelled')"
                                                            title="Cancel Appointment">
                                                            <i class="bi bi-calendar-x"></i>
                                                        </button>
                                                        <button class="btn-action-circle danger"
                                                            @click="deleteAppt(appt.id)"
                                                            title="Delete Appointment Record">
                                                            <i class="bi bi-trash3-fill"></i>
                                                        </button>
                                                    </div>
                                                </td>
                                            </tr>
                                            <tr v-if="filteredAppointments.length === 0">
                                                <td colspan="7" class="text-center text-muted py-5">
                                                    <i class="bi bi-calendar-x fs-2 d-block mb-2"></i>
                                                    No appointments found matching this status.
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Graphical status (Right) -->
                    <div class="col-xl-4">
                        <div class="card shadow-sm border-0 h-100">
                            <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
                                <i class="bi bi-pie-chart text-primary fs-5"></i>
                                <h5 class="mb-0 fw-bold text-dark">Appointment Status</h5>
                            </div>
                            <div class="card-body d-flex flex-column align-items-center justify-content-center p-4 bg-white">
                                <div style="width: 100%; max-width: 220px; height: 220px;" class="position-relative">
                                    <canvas id="appointmentsChart"></canvas>
                                </div>
                                <div class="mt-4 w-100 d-flex flex-column gap-2 text-muted small">
                                    <div class="d-flex justify-content-between">
                                        <span><i class="bi bi-circle-fill text-primary me-2"></i>Booked Visits</span>
                                        <strong class="text-dark">{{ appointments.filter(a => a.status === 'Booked').length }}</strong>
                                    </div>
                                    <div class="d-flex justify-content-between">
                                        <span><i class="bi bi-circle-fill text-success me-2"></i>Completed Visits</span>
                                        <strong class="text-dark">{{ appointments.filter(a => a.status === 'Completed').length }}</strong>
                                    </div>
                                    <div class="d-flex justify-content-between">
                                        <span><i class="bi bi-circle-fill text-danger me-2"></i>Cancelled Visits</span>
                                        <strong class="text-dark">{{ appointments.filter(a => a.status === 'Cancelled').length }}</strong>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- -----------------------------------------
                 TAB 2: DOCTORS MANAGEMENT
            ------------------------------------------ -->
            <div v-show="currentTab === 'doctors'" class="fade-in-up">
                <!-- Create Doctor Profile (Two-Column subtle Card) -->
                <div class="card shadow-sm border-0 mb-4">
                    <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
                        <i class="bi bi-person-plus text-primary fs-5"></i>
                        <h5 class="mb-0 fw-bold text-dark">Register New Doctor Profile</h5>
                    </div>
                    <div class="card-body p-4 bg-white">
                        <form @submit.prevent="addDoctor">
                            <div class="row g-4">
                                <!-- Col 1 -->
                                <div class="col-md-6 d-flex flex-column gap-3">
                                    <div>
                                        <label class="form-label text-secondary small fw-bold">Doctor Name</label>
                                        <div class="input-icon-wrapper">
                                            <i class="bi bi-person input-icon"></i>
                                            <input type="text" class="form-control" v-model="newDoc.username" placeholder="Dr. Jane Smith" required>
                                        </div>
                                    </div>
                                    <div>
                                        <label class="form-label text-secondary small fw-bold">Email Address</label>
                                        <div class="input-icon-wrapper">
                                            <i class="bi bi-envelope input-icon"></i>
                                            <input type="email" class="form-control" v-model="newDoc.email" placeholder="doctor@hospital.com" required>
                                        </div>
                                    </div>
                                    <div>
                                        <label class="form-label text-secondary small fw-bold">Create Password</label>
                                        <div class="input-icon-wrapper position-relative">
                                            <i class="bi bi-key input-icon"></i>
                                            <input :type="showPassword ? 'text' : 'password'" class="form-control pe-5" v-model="newDoc.password" placeholder="Or leave blank to auto-generate" required>
                                            <button type="button" class="btn btn-link position-absolute end-0 top-50 translate-middle-y text-muted p-0 me-3 border-0" @click="showPassword = !showPassword" style="background: transparent;">
                                                <i class="bi" :class="showPassword ? 'bi-eye-slash-fill' : 'bi-eye-fill'"></i>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- Col 2 -->
                                <div class="col-md-6 d-flex flex-column gap-3">
                                    <div>
                                        <label class="form-label text-secondary small fw-bold">Department Selection</label>
                                        <select class="form-select" v-model="newDoc.department_name" required>
                                            <option value="" disabled selected>Select Department</option>
                                            <option value="General Medicine">General Medicine</option>
                                            <option value="Cardiology">Cardiology</option>
                                            <option value="Neurology">Neurology</option>
                                            <option value="Dermatology">Dermatology</option>
                                            <option value="Pediatrics">Pediatrics</option>
                                            <option value="Dentistry">Dentistry</option>
                                        </select>
                                    </div>
                                    <div>
                                        <label class="form-label text-secondary small fw-bold">Availability Day(s)</label>
                                        <select class="form-select" v-model="newDoc.availability" required>
                                            <option value="" disabled selected>Select Working Day</option>
                                            <option value="Monday">Monday</option>
                                            <option value="Tuesday">Tuesday</option>
                                            <option value="Wednesday">Wednesday</option>
                                            <option value="Thursday">Thursday</option>
                                            <option value="Friday">Friday</option>
                                            <option value="Saturday">Saturday</option>
                                            <option value="Sunday">Sunday</option>
                                            <option value="Everyday">Everyday (7 Days)</option>
                                        </select>
                                    </div>
                                    <div>
                                        <label class="form-label text-secondary small fw-bold">Time Availability (Hours)</label>
                                        <div class="input-icon-wrapper">
                                            <i class="bi bi-clock input-icon"></i>
                                            <input type="text" class="form-control" v-model="newDoc.time_availability" placeholder="e.g. 10:00 AM - 09:00 PM" required>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="col-12 text-end">
                                    <button type="submit" class="btn btn-primary px-4 py-2 mt-2 shadow-sm fw-bold">
                                        <i class="bi bi-save2 me-2"></i>Save Doctor Profile
                                    </button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>

                <!-- Search Doctor Section -->
                <div class="card shadow-sm border-0 mb-4">
                    <div class="card-body p-4 bg-white">
                        <div class="d-flex flex-column flex-md-row gap-3 align-items-md-center justify-content-between">
                            <div class="flex-grow-1" style="max-width: 600px;">
                                <div class="input-group">
                                    <span class="input-group-text bg-light border-1"><i class="bi bi-search text-muted"></i></span>
                                    <input type="text" class="form-control" v-model="searchDocQuery" placeholder="Search doctors by specialization or name..." @keyup.enter="searchDoctors">
                                    <button class="btn btn-primary" @click="searchDoctors">Search</button>
                                </div>
                            </div>
                        </div>

                        <!-- Doctor Search Results list -->
                        <div class="search-results-list mt-3" v-if="docSearchResults.length">
                            <h6 class="text-muted small fw-bold text-uppercase mb-2">Search Results:</h6>
                            <ul class="list-group">
                                <li class="list-group-item d-flex justify-content-between align-items-center rounded-3 mb-2 border p-3 bg-light" v-for="d in docSearchResults" :key="d.id">
                                    <div class="d-flex align-items-center gap-3">
                                        <div class="bg-primary text-white rounded-circle d-flex align-items-center justify-content-center" style="width: 40px; height: 40px;">
                                            <i class="bi bi-person-fill"></i>
                                        </div>
                                        <div>
                                            <strong class="text-dark">{{ d.name }}</strong>
                                            <span class="badge bg-secondary ms-2">{{ d.specialization }}</span>
                                        </div>
                                    </div>
                                    <span class="text-muted small">Doc ID: {{ d.id }}</span>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Doctors Table with Inline Icons -->
                <div class="card shadow-sm border-0">
                    <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
                        <i class="bi bi-list-stars text-primary fs-5"></i>
                        <h5 class="mb-0 fw-bold text-dark">Registered Doctors</h5>
                    </div>
                    <div class="card-body p-0 bg-white">
                        <div class="table-responsive border-0">
                            <table class="table table-hover table-striped mb-0">
                                <thead>
                                    <tr>
                                        <th style="width: 90px;">Doc ID</th>
                                        <th>Profile Details</th>
                                        <th>Department</th>
                                        <th>Working Day</th>
                                        <th>Working Hours</th>
                                        <th class="text-end">Actions</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="doc in doctors" :key="doc.id" class="align-middle">
                                        <td class="fw-bold text-muted">#{{ doc.id }}</td>
                                        <td>
                                            <div v-if="doc.isEditing" class="d-flex flex-column gap-1" style="max-width: 200px;">
                                                <input type="text" class="form-control form-control-sm mb-1" v-model="doc.name">
                                                <span class="text-muted small">User ID: {{ doc.user_id }}</span>
                                            </div>
                                            <div v-else class="d-flex align-items-center gap-2">
                                                <div class="bg-light text-primary rounded-circle d-flex align-items-center justify-content-center" style="width: 34px; height: 34px;">
                                                    <i class="bi bi-person"></i>
                                                </div>
                                                <div>
                                                    <strong class="text-dark d-block">{{ doc.name }}</strong>
                                                    <span class="text-muted small">User ID: {{ doc.user_id }}</span>
                                                </div>
                                            </div>
                                        </td>
                                        <td>
                                            <span class="badge bg-primary-light text-primary font-heading rounded-pill px-3">{{ doc.department }}</span>
                                        </td>
                                        <td>
                                            <div v-if="doc.isEditing">
                                                <select class="form-select form-select-sm" v-model="doc.availability">
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
                                            <div v-else class="fw-medium text-dark">
                                                <i class="bi bi-calendar-check text-muted me-1 small"></i>
                                                {{ doc.availability || 'Not Set' }}
                                            </div>
                                        </td>
                                        <td>
                                            <div v-if="doc.isEditing">
                                                <input type="text" class="form-control form-control-sm" v-model="doc.time_availability">
                                            </div>
                                            <div v-else class="text-muted small">
                                                <i class="bi bi-clock text-muted me-1"></i>
                                                {{ doc.time_availability || 'Not Set' }}
                                            </div>
                                        </td>
                                        <td class="text-end">
                                            <div class="d-flex justify-content-end gap-2">
                                                <button v-if="!doc.isEditing" class="btn-action-circle primary"
                                                     @click="doc.isEditing = true"
                                                     title="Edit Profile">
                                                     <i class="bi bi-pencil-fill"></i>
                                                 </button>
                                                 <button v-if="doc.isEditing" class="btn-action-circle success"
                                                     @click="doc.isEditing = false; updateDoctor(doc.id, doc.name, doc.department, doc.availability, doc.time_availability)"
                                                     title="Save Profile">
                                                     <i class="bi bi-check-lg"></i>
                                                 </button>
                                                 <button v-if="doc.isEditing" class="btn-action-circle"
                                                     @click="doc.isEditing = false"
                                                     title="Cancel">
                                                     <i class="bi bi-x-lg"></i>
                                                 </button>
                                                 <button class="btn-action-circle danger"
                                                     @click="removeUser(doc.user_id)"
                                                     title="Remove Profile">
                                                     <i class="bi bi-trash3-fill"></i>
                                                 </button>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr v-if="doctors.length === 0">
                                        <td colspan="6" class="text-center text-muted py-5">
                                            <i class="bi bi-person-x fs-2 d-block mb-2"></i>
                                            No doctors registered yet.
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>

            <!-- -----------------------------------------
                 TAB 3: PATIENTS MANAGEMENT
            ------------------------------------------ -->
            <div v-show="currentTab === 'patients'" class="fade-in-up">
                <!-- Search Patient Panel -->
                <div class="card shadow-sm border-0 mb-4">
                    <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
                        <i class="bi bi-search-heart text-primary fs-5"></i>
                        <h5 class="mb-0 fw-bold text-dark">Search Patient Profiles</h5>
                    </div>
                    <div class="card-body p-4 bg-white">
                        <div class="input-group mb-3" style="max-width: 600px;">
                            <span class="input-group-text bg-light border-1"><i class="bi bi-search text-muted"></i></span>
                            <input type="text" class="form-control" v-model="searchPatQuery" placeholder="Search patients by contact number, ID, or name..." @keyup.enter="searchPatients">
                            <button class="btn btn-primary" @click="searchPatients">Search</button>
                        </div>
                        
                        <!-- Search Results list with Inline Icons -->
                        <div class="search-results mt-4" v-if="patSearchResults.length">
                            <h6 class="text-muted small fw-bold text-uppercase mb-2">Matching Records:</h6>
                            <ul class="list-group">
                                <li class="list-group-item bg-light border rounded-3 p-3 mb-2" v-for="p in patSearchResults" :key="p.id">
                                    <div class="row align-items-center g-3">
                                        <div class="col-md-3">
                                            <label class="form-label small text-muted mb-0">Name</label>
                                            <input type="text" class="form-control form-control-sm mt-1" v-model="p.name" placeholder="Name">
                                        </div>
                                        <div class="col-md-3">
                                            <label class="form-label small text-muted mb-0">Contact</label>
                                            <input type="text" class="form-control form-control-sm mt-1" v-model="p.contact" placeholder="Contact">
                                        </div>
                                        <div class="col-md-3">
                                            <label class="form-label small text-muted mb-0">Address</label>
                                            <input type="text" class="form-control form-control-sm mt-1" v-model="p.address" placeholder="Address">
                                        </div>
                                        <div class="col-md-3 d-flex gap-2 justify-content-end align-self-end mt-2 mt-md-0">
                                            <button class="btn-action-circle success"
                                                @click="updatePatient(p)"
                                                title="Save Patient Info">
                                                <i class="bi bi-check-lg"></i>
                                            </button>
                                            <button class="btn-action-circle danger"
                                                @click="removeUser(p.user_id)"
                                                title="Remove Patient Profile">
                                                <i class="bi bi-trash3-fill"></i>
                                            </button>
                                        </div>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- All Registered Patients Table with Inline Icons -->
                <div class="card shadow-sm border-0">
                    <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
                        <i class="bi bi-people-fill text-primary fs-5"></i>
                        <h5 class="mb-0 fw-bold text-dark">Registered Patients List</h5>
                    </div>
                    <div class="card-body p-0 bg-white">
                        <div class="table-responsive border-0">
                            <table class="table table-hover table-striped mb-0">
                                <thead>
                                    <tr>
                                        <th style="width: 90px;">PID</th>
                                        <th>Patient Name</th>
                                        <th>Email Address</th>
                                        <th>Contact Number</th>
                                        <th>Home Address</th>
                                        <th class="text-end">Actions</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="pat in patients" :key="pat.id" class="align-middle">
                                        <td class="fw-bold text-muted">#{{ pat.id }}</td>
                                        <td>
                                            <div class="d-flex align-items-center" style="max-width: 200px;">
                                                <input type="text" class="form-control form-control-sm font-heading fw-bold" v-model="pat.name">
                                            </div>
                                        </td>
                                        <td class="text-muted small">{{ pat.email }}</td>
                                        <td>
                                            <input type="text" class="form-control form-control-sm" v-model="pat.contact" style="max-width: 140px;">
                                        </td>
                                        <td>
                                            <input type="text" class="form-control form-control-sm" v-model="pat.address">
                                        </td>
                                        <td class="text-end">
                                            <div class="d-flex justify-content-end gap-2">
                                                 <button class="btn-action-circle success"
                                                     @click="updatePatient(pat)"
                                                     title="Save Profile">
                                                     <i class="bi bi-check-lg"></i>
                                                 </button>
                                                 <button class="btn-action-circle danger"
                                                     @click="removeUser(pat.user_id)"
                                                     title="Remove Patient">
                                                     <i class="bi bi-trash3-fill"></i>
                                                 </button>
                                             </div>
                                        </td>
                                    </tr>
                                    <tr v-if="patients.length === 0">
                                        <td colspan="6" class="text-center text-muted py-5">
                                            <i class="bi bi-people-fill fs-2 d-block mb-2"></i>
                                            No patients registered.
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
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
            currentTab: 'overview',
            token: localStorage.getItem('access_token'),
            error: '', success: '',
            stats: { total_patients: 0, total_doctors: 0, total_appointments: 0 },
            newDoc: { username: '', email: '', password: '', specialization: '', department_name: '', availability: '', time_availability: '' },
            appointments: [],
            doctors: [],
            appointmentFilter: 'Booked',
            searchDocQuery: '', docSearchResults: [],
            searchPatQuery: '', patSearchResults: [],
            patients: [],
            showPassword: false,
            chartInstance: null,
            showThemeCustomizer: false,
            isDarkMode: false,
            activeAccent: 'indigo',
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

        getDocSpecialization(docName) {
            const doc = this.doctors.find(d => d.name === docName);
            return doc ? doc.specialization : 'General Medicine';
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

        async fetchData() {
            try {
                const res1 = await fetch('http://127.0.0.1:5000/api/admin/dashboard', { headers: this.authHeader() });
                this.stats = await res1.json();

                const res2 = await fetch('http://127.0.0.1:5000/api/admin/appointments', { headers: this.authHeader() });
                this.appointments = await res2.json();

                const res3 = await fetch('http://127.0.0.1:5000/api/admin/doctors', { headers: this.authHeader() });
                this.doctors = await res3.json();

                const res4 = await fetch('http://127.0.0.1:5000/api/admin/patients', { headers: this.authHeader() });
                this.patients = await res4.json();

                this.$nextTick(() => {
                    this.renderChart();
                });
            } catch (e) { this.showMsg('error', "Loading data..."); } 
        },
        renderChart() {
            const ctx = document.getElementById('appointmentsChart');
            if (!ctx) return;
            
            const booked = this.appointments.filter(a => a.status === 'Booked').length;
            const completed = this.appointments.filter(a => a.status === 'Completed').length;
            const cancelled = this.appointments.filter(a => a.status === 'Cancelled').length;
            
            if (this.chartInstance) {
                this.chartInstance.data.datasets[0].data = [booked, completed, cancelled];
                this.chartInstance.update();
                return;
            }
            
            this.chartInstance = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Booked', 'Completed', 'Cancelled'],
                    datasets: [{
                        data: [booked, completed, cancelled],
                        backgroundColor: ['#6366f1', '#10b981', '#f43f5e'],
                        borderWidth: 2,
                        borderColor: '#ffffff'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false
                        }
                    },
                    cutout: '75%'
                }
            });
        },
        async addDoctor() {
            try {
                const payload = {
                    username: this.newDoc.username,
                    email: this.newDoc.email,
                    password: this.newDoc.password,
                    specialization: this.newDoc.department_name || 'General',
                    department_name: this.newDoc.department_name,
                    availability: this.newDoc.availability,
                    time_availability: this.newDoc.time_availability
                };
                const res = await fetch('http://127.0.0.1:5000/api/admin/doctor', {
                    method: 'POST', headers: this.authHeader(), body: JSON.stringify(payload)
                });
                const data = await res.json();
                if (res.ok) {
                    this.showMsg('success', "Doctor account created! Password generated: " + data.generated_password); 
                    alert("DOCTOR SAVED SUCCESSFULLY!\n\nEmail: " + this.newDoc.email + "\nPassword: " + data.generated_password);
                    this.newDoc = { username: '', email: '', password: '', department_name: '', availability: '', time_availability: '' };
                    this.fetchData();
                }
                else if (res.status === 401) {
                    alert("SESSION EXPIRED:You will be logged out now. Please log in again.");
                    this.logout();
                }
                else {
                    this.showMsg('error', data.message || data.msg || "Server rejection");
                    alert("ERROR SAVING DOCTOR: " + (data.message || data.msg || "Server rejection"));
                }
            } catch (e) {
                this.showMsg('error', "Failed to run POST.");
                alert("NETWORK ERROR: Cannot reach Server.");
            }
            window.scrollTo({ top: 0, behavior: 'smooth' });
        },
        async updateDoctor(doc_id, name, spec, avail, time_avail) {
            try {
                const res = await fetch('http://127.0.0.1:5000/api/admin/doctor/' + doc_id, {
                    method: 'PUT', headers: this.authHeader(), body: JSON.stringify({ name: name, specialization: spec, availability: avail, time_availability: time_avail })
                });
                if (res.ok) { this.showMsg('success', "Doctor profile updated!"); this.fetchData(); }
                else { const data = await res.json(); this.showMsg('error', data.message); }
            } catch (e) { this.showMsg('error', "Network error."); }
        },
        async searchDoctors() {
            if (!this.searchDocQuery) return;
            const res = await fetch('http://127.0.0.1:5000/api/admin/doctors/search?q=' + this.searchDocQuery, { headers: this.authHeader() });
            if (res.ok) {
                this.docSearchResults = await res.json();
                if (this.docSearchResults.length === 0) {
                    alert('No doctor found');
                }
            }
        },
        async searchPatients() {
            if (!this.searchPatQuery) return;
            const res = await fetch('http://127.0.0.1:5000/api/admin/patients/search?q=' + this.searchPatQuery, { headers: this.authHeader() });
            if (res.ok) {
                this.patSearchResults = await res.json();
                if (this.patSearchResults.length === 0) {
                    alert('Patient not found');
                }
            }
        },
        async updatePatient(p) {
            try {
                const res = await fetch('http://127.0.0.1:5000/api/admin/patient/' + p.id, {
                    method: 'PUT', headers: this.authHeader(), body: JSON.stringify({ name: p.name, contact: p.contact, address: p.address })
                });
                if (res.ok) { this.showMsg('success',"Patient profile updated."); }
                else { const data = await res.json(); this.showMsg('error', data.message); }
            } catch (e) { this.showMsg('error', "Network error"); }
        },
        async removeUser(user_id) {
            if (confirm("DANGER: Permanently remove this profile?")) {
                const res = await fetch('http://127.0.0.1:5000/api/admin/user/' + user_id, { method: 'DELETE', headers: this.authHeader() });
                if (res.ok) { this.showMsg('success', "Profile removed from the hospital records."); this.fetchData(); }
                else { const data = await res.json(); this.showMsg('error', data.message); }
            }
        },
        async deleteAppt(id) {
            if (confirm("Erase this booking?")) {
                await fetch('http://127.0.0.1:5000/api/admin/appointment/' + id, { method: 'DELETE', headers: this.authHeader() });
                this.fetchData(); 
            }
        },
        async updateAppointmentStatus(id, status) {
            const res = await fetch('http://127.0.0.1:5000/api/appointments/' + id + '/status', {
                method: 'PATCH', headers: this.authHeader(), body: JSON.stringify({ status: status })
            });
            if (res.ok) {
                this.showMsg('success', 'Appointment updated successfully!');
                this.fetchData();
            } else {
                const data = await res.json();
                this.showMsg('error', data.message || 'Failed to update appointment');
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
    computed: {
        filteredAppointments() {
            if (this.appointmentFilter === 'All') return this.appointments;
            return this.appointments.filter(a => a.status === this.appointmentFilter);
        }
    },
    mounted() {
        this.loadTheme();
        if (!this.token || localStorage.getItem('role') !== 'Admin') this.logout();
        else this.fetchData();
    }
}
</script>

<style scoped>
.admin-dashboard-wrapper {
    min-height: 100vh;
    background-color: #f8fafc;
}

.stat-card {
    transition: var(--transition-smooth);
}

.stat-icon-container {
    width: 60px;
    height: 60px;
    border-radius: 14px;
    display: grid;
    place-items: center;
}

.bg-primary-light {
    background-color: rgba(71, 85, 105, 0.08) !important;
    color: #475569 !important;
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

.nav-brand-icon {
    background: linear-gradient(135deg, #64748b 0%, #475569 100%) !important;
}

/* Animations */
.fade-enter-active, .fade-leave-active { transition: opacity 0.3s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
</style>
