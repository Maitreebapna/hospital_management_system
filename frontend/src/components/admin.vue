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
                <!-- Clean Minimalist Sub-Tab Navigation Header -->
                <div class="doc-sub-nav d-flex align-items-center justify-content-between mb-4 border-bottom pb-2">
                    <div class="d-flex align-items-center gap-3">
                        <button class="doc-sub-nav-btn" :class="{ active: docSubTab === 'directory' }" @click="docSubTab = 'directory'">
                            <i class="bi bi-person-badge-fill me-2"></i>
                            <span>Doctor Directory</span>
                            <span class="badge rounded-pill bg-light text-dark ms-2" style="font-size: 11px !important;">{{ doctors.length }}</span>
                        </button>
                        <button class="doc-sub-nav-btn" :class="{ active: docSubTab === 'register' }" @click="docSubTab = 'register'">
                            <i class="bi bi-person-plus-fill me-2"></i>
                            <span>Register New Doctor</span>
                        </button>
                    </div>
                    <span class="text-muted small fw-medium d-none d-md-inline">
                        <i class="bi bi-info-circle me-1"></i>Manage schedules and specialties
                    </span>
                </div>

                <!-- SUB-TAB 1: DOCTOR DIRECTORY -->
                <div v-show="docSubTab === 'directory'" class="fade-in-up">
                    <!-- Doctor Dashboard Statistics Strip -->
                    <div class="row g-3 mb-4">
                        <div class="col-6 col-md-3">
                            <div class="card stat-card border-0 shadow-sm mb-0 bg-pastel-blue" style="border-left: 4px solid var(--theme-primary) !important;">
                                <div class="card-body p-3 d-flex align-items-center justify-content-between">
                                    <div>
                                        <span class="text-muted small fw-bold text-uppercase d-block" style="font-size: 11px !important;">Total Doctors</span>
                                        <h4 class="fw-extrabold text-dark mb-0">{{ doctors.length }}</h4>
                                    </div>
                                    <div class="stat-icon-container bg-primary-light text-primary" style="width: 42px; height: 42px; border-radius: 10px;">
                                        <i class="bi bi-person-badge-fill fs-5"></i>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-6 col-md-3">
                            <div class="card stat-card border-0 shadow-sm mb-0 bg-pastel-green" style="border-left: 4px solid #10b981 !important;">
                                <div class="card-body p-3 d-flex align-items-center justify-content-between">
                                    <div>
                                        <span class="text-muted small fw-bold text-uppercase d-block" style="font-size: 11px !important;">Departments</span>
                                        <h4 class="fw-extrabold text-dark mb-0">6</h4>
                                    </div>
                                    <div class="stat-icon-container bg-success-subtle text-success" style="width: 42px; height: 42px; border-radius: 10px; border: none;">
                                        <i class="bi bi-hospital fs-5"></i>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-6 col-md-3">
                            <div class="card stat-card border-0 shadow-sm mb-0 bg-pastel-purple" style="border-left: 4px solid #8b5cf6 !important;">
                                <div class="card-body p-3 d-flex align-items-center justify-content-between">
                                    <div>
                                        <span class="text-muted small fw-bold text-uppercase d-block" style="font-size: 11px !important;">Everyday Duty</span>
                                        <h4 class="fw-extrabold text-dark mb-0">{{ doctors.filter(d => d.availability === 'Everyday').length }}</h4>
                                    </div>
                                    <div class="stat-icon-container bg-primary-subtle text-primary" style="width: 42px; height: 42px; border-radius: 10px; border: none;">
                                        <i class="bi bi-calendar-range fs-5"></i>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-6 col-md-3">
                            <div class="card stat-card border-0 shadow-sm mb-0 bg-pastel-pink" style="border-left: 4px solid #f43f5e !important;">
                                <div class="card-body p-3 d-flex align-items-center justify-content-between">
                                    <div>
                                        <span class="text-muted small fw-bold text-uppercase d-block" style="font-size: 11px !important;">Active Slots</span>
                                        <h4 class="fw-extrabold text-dark mb-0">Morning/Evening</h4>
                                    </div>
                                    <div class="stat-icon-container bg-danger-subtle text-danger" style="width: 42px; height: 42px; border-radius: 10px; border: none;">
                                        <i class="bi bi-clock-history fs-5"></i>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Server Search results alert indicator -->
                    <div v-if="docSearchResults.length" class="alert alert-info border-0 shadow-sm d-flex justify-content-between align-items-center mb-3">
                        <div>
                            <i class="bi bi-search me-2 fs-5"></i>
                            <span>Found <strong>{{ docSearchResults.length }}</strong> match(es) from server.</span>
                        </div>
                        <button class="btn btn-sm btn-outline-info text-dark" @click="docSearchResults = []">Reset Search</button>
                    </div>

                    <!-- Unified Control Bar -->
                    <div class="card shadow-sm border-0 mb-3 bg-pastel-slate">
                        <div class="card-body p-3 d-flex flex-column flex-md-row align-items-center justify-content-between gap-3">
                            <!-- Modern search input -->
                            <div class="w-100 flex-grow-1" style="max-width: 450px;">
                                <div class="input-group search-bar-premium">
                                    <span class="input-group-text bg-transparent border-end-0"><i class="bi bi-search text-muted"></i></span>
                                    <input type="text" class="form-control border-start-0 border-end-0" v-model="searchDocQuery" placeholder="Search by name, specialization, ID...">
                                    <button v-if="searchDocQuery" class="btn btn-link text-muted border-start-0 border-end-0" @click="searchDocQuery = ''" style="background: transparent; z-index: 10;">
                                        <i class="bi bi-x-circle-fill"></i>
                                    </button>
                                    <button class="btn btn-primary" @click="searchDoctors">Search DB</button>
                                </div>
                            </div>
                            <!-- View Toggle -->
                            <div class="d-flex align-items-center gap-2">
                                <span class="text-muted small fw-bold text-uppercase d-none d-sm-inline">Layout:</span>
                                <div class="btn-group view-switcher-group shadow-sm p-1 rounded-3 bg-light border" role="group">
                                    <button class="btn btn-sm btn-view-mode" :class="{ active: viewMode === 'grid' }" @click="viewMode = 'grid'">
                                        <i class="bi bi-grid-fill me-1"></i> Grid
                                    </button>
                                    <button class="btn btn-sm btn-view-mode" :class="{ active: viewMode === 'table' }" @click="viewMode = 'table'">
                                        <i class="bi bi-list-task me-1"></i> List
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Department Filter Pills -->
                    <div class="dept-pills-container mb-4">
                        <button v-for="dept in departments" 
                                :key="dept" 
                                class="dept-pill-btn" 
                                :class="{ active: selectedDeptFilter === dept }"
                                @click="selectedDeptFilter = dept">
                            <span class="dept-pill-text">{{ dept }}</span>
                            <span class="badge rounded-pill bg-light text-dark ms-1 small" v-if="selectedDeptFilter === dept" style="font-size: 10px !important;">
                                {{ dept === 'All' ? doctors.length : doctors.filter(d => d.department === dept).length }}
                            </span>
                        </button>
                    </div>

                    <!-- View 1: Card-Based Directory Grid -->
                    <div v-if="viewMode === 'grid'" class="doctor-card-grid fade-in-up">
                        <div v-for="doc in filteredDoctors" :key="doc.id" :class="['doctor-profile-card', 'shadow-sm', 'border-0', 'h-100', getDocCardBgClass(doc.department)]">
                            <!-- Top Info Header -->
                            <div class="doctor-card-header">
                                <div class="doctor-avatar-wrapper">
                                    <div class="doctor-card-avatar">
                                        {{ doc.name ? doc.name.split(' ').pop().charAt(0).toUpperCase() : 'D' }}
                                    </div>
                                    <span class="doctor-badge-status"></span>
                                </div>
                                <div class="overflow-hidden w-100">
                                    <div v-if="doc.isEditing">
                                        <input type="text" class="form-control form-control-sm mb-1" v-model="doc.name">
                                    </div>
                                    <strong v-else class="text-dark d-block text-truncate fs-5" style="font-weight: 700 !important;">{{ doc.name }}</strong>
                                    <span class="text-muted small d-block">ID: #{{ doc.id }} (User: {{ doc.user_id }})</span>
                                </div>
                            </div>

                            <!-- Department Badge & Availability details -->
                            <div class="doctor-schedule-section">
                                <div class="mb-2">
                                    <div v-if="doc.isEditing">
                                        <select class="form-select form-select-sm" v-model="doc.department">
                                            <option value="General Medicine">General Medicine</option>
                                            <option value="Cardiology">Cardiology</option>
                                            <option value="Neurology">Neurology</option>
                                            <option value="Dermatology">Dermatology</option>
                                            <option value="Pediatrics">Pediatrics</option>
                                            <option value="Dentistry">Dentistry</option>
                                        </select>
                                    </div>
                                    <span v-else class="badge" :class="getDeptBadgeClass(doc.department)">
                                        {{ doc.department }}
                                    </span>
                                </div>

                                <!-- Working Day -->
                                <div class="schedule-item">
                                    <i class="bi bi-calendar-check"></i>
                                    <div v-if="doc.isEditing" class="w-100">
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
                                    <span v-else class="fw-medium text-dark">{{ doc.availability || 'Not Set' }}</span>
                                </div>

                                <!-- Working Hours -->
                                <div class="schedule-item">
                                    <i class="bi bi-clock"></i>
                                    <div v-if="doc.isEditing" class="w-100">
                                        <input type="text" class="form-control form-control-sm" v-model="doc.time_availability">
                                    </div>
                                    <span v-else class="text-muted">{{ doc.time_availability || 'Not Set' }}</span>
                                </div>
                            </div>

                            <!-- Card Action buttons at bottom -->
                            <div class="doctor-card-actions">
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
                        </div>
                    </div>

                    <!-- View 2: Compact List/Table View -->
                    <div v-if="viewMode === 'table'" class="card shadow-sm border-0 fade-in-up bg-pastel-slate">
                        <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
                            <i class="bi bi-list-stars text-primary fs-5"></i>
                            <h5 class="mb-0 fw-bold text-dark">Registered Doctors List</h5>
                        </div>
                        <div class="card-body p-0">
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
                                        <tr v-for="doc in filteredDoctors" :key="doc.id" class="align-middle">
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
                                                        <strong class="text-dark d-block" style="font-weight: 700 !important;">{{ doc.name }}</strong>
                                                        <span class="text-muted small">User ID: {{ doc.user_id }}</span>
                                                    </div>
                                                </div>
                                            </td>
                                            <td>
                                                <div v-if="doc.isEditing">
                                                    <select class="form-select form-select-sm" v-model="doc.department">
                                                        <option value="General Medicine">General Medicine</option>
                                                        <option value="Cardiology">Cardiology</option>
                                                        <option value="Neurology">Neurology</option>
                                                        <option value="Dermatology">Dermatology</option>
                                                        <option value="Pediatrics">Pediatrics</option>
                                                        <option value="Dentistry">Dentistry</option>
                                                    </select>
                                                </div>
                                                <span v-else class="badge" :class="getDeptBadgeClass(doc.department)">{{ doc.department }}</span>
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
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>

                    <!-- No Results State -->
                    <div v-if="filteredDoctors.length === 0" class="card shadow-sm border-0 p-5 text-center bg-white mt-3">
                        <div class="card-body">
                            <i class="bi bi-person-x fs-1 text-muted d-block mb-3"></i>
                            <h5 class="fw-bold text-dark">No Doctors Found</h5>
                            <p class="text-muted small">We couldn't find any doctor profiles matching the current search filters.</p>
                            <button class="btn btn-sm btn-primary mt-2" @click="searchDocQuery = ''; selectedDeptFilter = 'All'">
                                Reset Filters
                            </button>
                        </div>
                    </div>
                </div>

                <!-- SUB-TAB 2: REGISTER NEW DOCTOR -->
                <div v-show="docSubTab === 'register'" class="fade-in-up">
                    <div class="row justify-content-center">
                        <div class="col-lg-8 col-xl-7">
                            <div class="card shadow border-0 register-premium-card bg-pastel-blue">
                                <div class="card-header bg-white border-bottom p-4 d-flex align-items-center gap-3">
                                    <div class="stat-icon-container bg-primary-light text-primary" style="width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center;">
                                        <i class="bi bi-person-plus-fill fs-4"></i>
                                    </div>
                                    <div>
                                        <h5 class="mb-0 fw-bold text-dark" style="font-size: 18px !important;">Register Doctor Profile</h5>
                                        <span class="text-muted small">Create a new credentials profile and availability schedule</span>
                                    </div>
                                </div>
                                <div class="card-body p-4">
                                    <form @submit.prevent="addDoctor">
                                        <div class="row g-4">
                                            <!-- Doctor Name -->
                                            <div class="col-md-6">
                                                <label class="form-label text-secondary small fw-bold">Doctor Name</label>
                                                <div class="input-icon-wrapper">
                                                    <i class="bi bi-person input-icon"></i>
                                                    <input type="text" class="form-control" v-model="newDoc.username" placeholder="Dr. Jane Smith" required>
                                                </div>
                                            </div>
                                            <!-- Email Address -->
                                            <div class="col-md-6">
                                                <label class="form-label text-secondary small fw-bold">Email Address</label>
                                                <div class="input-icon-wrapper">
                                                    <i class="bi bi-envelope input-icon"></i>
                                                    <input type="email" class="form-control" v-model="newDoc.email" placeholder="doctor@hospital.com" required>
                                                </div>
                                            </div>
                                            <!-- Password -->
                                            <div class="col-md-6">
                                                <label class="form-label text-secondary small fw-bold">Create Password</label>
                                                <div class="input-icon-wrapper position-relative">
                                                    <i class="bi bi-key input-icon"></i>
                                                    <input :type="showPassword ? 'text' : 'password'" class="form-control pe-5" v-model="newDoc.password" placeholder="Or leave blank to auto-generate" required>
                                                    <button type="button" class="btn btn-link position-absolute end-0 top-50 translate-middle-y text-muted p-0 me-3 border-0" @click="showPassword = !showPassword" style="background: transparent;">
                                                        <i class="bi" :class="showPassword ? 'bi-eye-slash-fill' : 'bi-eye-fill'"></i>
                                                    </button>
                                                </div>
                                            </div>
                                            <!-- Department Selection -->
                                            <div class="col-md-6">
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
                                            <!-- Availability Day(s) -->
                                            <div class="col-md-6">
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
                                            <!-- Time Availability -->
                                            <div class="col-md-6">
                                                <label class="form-label text-secondary small fw-bold">Time Availability (Hours)</label>
                                                <div class="input-icon-wrapper">
                                                    <i class="bi bi-clock input-icon"></i>
                                                    <input type="text" class="form-control" v-model="newDoc.time_availability" placeholder="e.g. 10:00 AM - 09:00 PM" required>
                                                </div>
                                            </div>
                                            
                                            <div class="col-12 mt-4 text-end">
                                                <button type="submit" class="btn btn-primary px-4 py-2.5 shadow-sm fw-bold">
                                                    <i class="bi bi-plus-circle me-2"></i>Register Profile
                                                </button>
                                            </div>
                                        </div>
                                    </form>
                                </div>
                            </div>
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
            isDarkMode: false,
            viewMode: 'grid',
            docSubTab: 'directory',
            selectedDeptFilter: 'All',
            departments: ['All', 'General Medicine', 'Cardiology', 'Neurology', 'Dermatology', 'Pediatrics', 'Dentistry']
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
        getDeptBadgeClass(dept) {
            switch(dept) {
                case 'Cardiology': return 'badge-pastel-pink';
                case 'Neurology': return 'badge-pastel-purple';
                case 'Dermatology': return 'badge-pastel-green';
                case 'Pediatrics': return 'badge-pastel-violet';
                case 'Dentistry': return 'badge-pastel-brown';
                case 'General Medicine': return 'badge-pastel-blue';
                default: return 'badge-pastel-slate';
            }
        },
        getDocCardBgClass(dept) {
            switch(dept) {
                case 'Cardiology': return 'bg-pastel-pink';
                case 'Neurology': return 'bg-pastel-purple';
                case 'Dermatology': return 'bg-pastel-green';
                case 'Pediatrics': return 'bg-pastel-violet';
                case 'Dentistry': return 'bg-pastel-brown';
                case 'General Medicine': return 'bg-pastel-blue';
                default: return 'bg-pastel-slate';
            }
        }
    },
    computed: {
        filteredAppointments() {
            if (this.appointmentFilter === 'All') return this.appointments;
            return this.appointments.filter(a => a.status === this.appointmentFilter);
        },
        filteredDoctors() {
            let list = this.doctors;
            if (this.selectedDeptFilter && this.selectedDeptFilter !== 'All') {
                list = list.filter(d => d.department === this.selectedDeptFilter);
            }
            if (this.searchDocQuery) {
                const q = this.searchDocQuery.toLowerCase();
                list = list.filter(d => 
                    (d.name && d.name.toLowerCase().includes(q)) || 
                    (d.department && d.department.toLowerCase().includes(q)) ||
                    (d.id && d.id.toString().includes(q)) ||
                    (d.specialization && d.specialization.toLowerCase().includes(q))
                );
            }
            return list;
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

/* Redesigned Doctors Layout Scoped Style Overlays */
.dept-pills-container {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
}

.dept-pill-btn {
    border: 1.5px solid #e2e8f0;
    background-color: #ffffff;
    border-radius: 50px;
    padding: 0.45rem 1.1rem;
    font-size: 13.5px !important;
    font-weight: 600 !important;
    color: #4b5563;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    display: inline-flex;
    align-items: center;
    cursor: pointer;
}

.dept-pill-btn:hover {
    border-color: var(--theme-primary);
    color: var(--theme-primary);
    background-color: var(--theme-primary-light);
}

.dept-pill-btn.active {
    background: var(--theme-gradient) !important;
    color: #ffffff !important;
    border-color: transparent;
    box-shadow: 0 4px 10px rgba(79, 70, 229, 0.15);
}

.dept-pill-btn.active .badge {
    background-color: rgba(255, 255, 255, 0.25) !important;
    color: #ffffff !important;
}

.search-bar-premium {
    border: 1.5px solid #e2e8f0;
    border-radius: var(--border-radius-sm);
    overflow: hidden;
    background-color: #ffffff;
    transition: var(--transition-smooth);
}

.search-bar-premium:focus-within {
    border-color: var(--theme-primary);
    box-shadow: 0 0 0 4px var(--theme-primary-light);
}

.search-bar-premium .form-control {
    border: none !important;
    box-shadow: none !important;
    background: transparent !important;
}

.view-switcher-group .btn-view-mode {
    border-radius: 6px !important;
    font-size: 12.5px !important;
    font-weight: 700 !important;
    padding: 4px 12px !important;
    color: #6b7280 !important;
    background: transparent !important;
}

.view-switcher-group .btn-view-mode.active {
    background-color: #ffffff !important;
    color: var(--theme-primary) !important;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05) !important;
}

/* Card Directory */
.doctor-card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1.25rem;
}

.doctor-profile-card {
    background: #ffffff;
    border: 1px solid rgba(226, 232, 240, 0.8);
    border-radius: var(--border-radius-md);
    padding: 1.5rem;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    height: 100%;
}

.doctor-profile-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px -8px rgba(0, 0, 0, 0.08) !important;
    border-color: var(--theme-primary) !important;
}

.doctor-card-header {
    display: flex;
    align-items: center;
    gap: 0.85rem;
    margin-bottom: 1.15rem;
}

.doctor-avatar-wrapper {
    position: relative;
}

.doctor-card-avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background-color: var(--theme-primary-light);
    color: var(--theme-primary);
    font-size: 18px !important;
    font-weight: 700 !important;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid #ffffff;
    box-shadow: 0 0 0 2px var(--theme-primary-light);
    transition: var(--transition-smooth);
}

.doctor-profile-card:hover .doctor-card-avatar {
    transform: scale(1.05);
}

.doctor-badge-status {
    position: absolute;
    bottom: -2px;
    right: -2px;
    width: 13px;
    height: 13px;
    border-radius: 50%;
    background-color: #10b981;
    border: 2px solid #ffffff;
}

/* Schedule Details */
.doctor-schedule-section {
    display: flex;
    flex-direction: column;
    gap: 0.45rem;
    margin-bottom: 1.25rem;
    flex-grow: 1;
}

.schedule-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 13.5px !important;
    color: #4b5563;
}

.schedule-item i {
    font-size: 14.5px !important;
    color: #94a3b8;
}

/* Actions */
.doctor-card-actions {
    display: flex;
    justify-content: flex-end;
    gap: 0.5rem;
    border-top: 1px solid #f1f5f9;
    padding-top: 0.85rem;
    margin-top: auto;
}

/* Custom Department Badges overrides */
.badge.bg-primary-subtle {
    border-color: rgba(99, 102, 241, 0.2) !important;
}

/* Sticky positioning adjustment */
.sticky-top {
    position: -webkit-sticky;
    position: sticky;
    top: 24px;
    z-index: 10;
}

/* Dark Mode Additions */
body.dark-theme .doctor-profile-card {
    background-color: rgba(17, 24, 39, 0.85) !important;
    border-color: rgba(55, 65, 81, 0.4) !important;
}

body.dark-theme .dept-pill-btn {
    background-color: #1f2937 !important;
    border-color: #374151 !important;
    color: #d1d5db !important;
}

body.dark-theme .dept-pill-btn:hover {
    background-color: rgba(255, 255, 255, 0.05) !important;
    color: #ffffff !important;
}

body.dark-theme .view-switcher-group {
    background-color: #1f2937 !important;
    border-color: #374151 !important;
}

body.dark-theme .view-switcher-group .btn-view-mode {
    color: #9ca3af !important;
}

body.dark-theme .view-switcher-group .btn-view-mode.active {
    background-color: #111827 !important;
    color: #ffffff !important;
}

body.dark-theme .doctor-card-actions {
    border-top-color: #374151 !important;
}

body.dark-theme .doctor-card-avatar {
    border-color: #1f2937 !important;
    box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.05) !important;
}

/* Sub-Tab Navigation Header Styles */
.doc-sub-nav {
    border-bottom: 2px solid #e2e8f0;
}
.doc-sub-nav-btn {
    background: transparent;
    border: none;
    padding: 0.75rem 1.25rem;
    font-size: 14.5px !important;
    font-weight: 700 !important;
    color: #6b7280;
    position: relative;
    transition: all 0.2s ease;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
}
.doc-sub-nav-btn:hover {
    color: var(--theme-primary);
}
.doc-sub-nav-btn.active {
    color: var(--theme-primary);
}
.doc-sub-nav-btn.active::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    right: 0;
    height: 3px;
    background: var(--theme-gradient);
    border-radius: 3px 3px 0 0;
}
.doc-sub-nav-btn .badge {
    transition: all 0.2s ease;
}
.doc-sub-nav-btn.active .badge {
    background-color: var(--theme-primary-light) !important;
    color: var(--theme-primary) !important;
}

/* Premium centered registration card */
.register-premium-card {
    border-radius: var(--border-radius-lg) !important;
    overflow: hidden;
    background: #ffffff;
    border: 1px solid rgba(226, 232, 240, 0.8) !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.04) !important;
}
.register-premium-card .card-header {
    background: rgba(255,255,255,0.7) !important;
    border-bottom: 1.5px solid #f1f5f9 !important;
}

/* Dark theme overrides for sub-tabs */
body.dark-theme .doc-sub-nav {
    border-bottom-color: #374151;
}
body.dark-theme .doc-sub-nav-btn {
    color: #9ca3af;
}
body.dark-theme .doc-sub-nav-btn:hover,
body.dark-theme .doc-sub-nav-btn.active {
    color: #ffffff;
}
body.dark-theme .doc-sub-nav-btn.active .badge {
    background-color: rgba(255, 255, 255, 0.1) !important;
    color: #ffffff !important;
}
body.dark-theme .register-premium-card {
    background-color: rgba(17, 24, 39, 0.85) !important;
    border-color: rgba(55, 65, 81, 0.4) !important;
}
body.dark-theme .register-premium-card .card-header {
    background: rgba(31, 41, 55, 0.5) !important;
    border-bottom-color: #374151 !important;
}

/* Curated Soft Pastel Color Theme Styles */
.bg-pastel-pink {
    background-color: #fff1f2 !important;
    border: 1px solid #ffe4e6 !important;
}
.bg-pastel-purple {
    background-color: #faf5ff !important;
    border: 1px solid #f3e8ff !important;
}
.bg-pastel-green {
    background-color: #f0fdf4 !important;
    border: 1px solid #dcfce7 !important;
}
.bg-pastel-violet {
    background-color: #f5f3ff !important;
    border: 1px solid #e0e7ff !important;
}
.bg-pastel-brown {
    background-color: #faf6f0 !important;
    border: 1px solid #f5ebe0 !important;
}
.bg-pastel-blue {
    background-color: #eff6ff !important;
    border: 1px solid #dbeafe !important;
}
.bg-pastel-slate {
    background-color: #f8fafc !important;
    border: 1px solid #e2e8f0 !important;
}

/* Custom Badges matching the Pastel Themes */
.badge-pastel-pink {
    background-color: #ffe4e6 !important;
    color: #e11d48 !important;
    border: 1px solid #fecdd3 !important;
    padding: 0.35em 0.65em;
    font-size: .75em;
    font-weight: 700;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: .375rem;
}
.badge-pastel-purple {
    background-color: #f3e8ff !important;
    color: #7e22ce !important;
    border: 1px solid #e9d5ff !important;
    padding: 0.35em 0.65em;
    font-size: .75em;
    font-weight: 700;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: .375rem;
}
.badge-pastel-green {
    background-color: #dcfce7 !important;
    color: #15803d !important;
    border: 1px solid #bbf7d0 !important;
    padding: 0.35em 0.65em;
    font-size: .75em;
    font-weight: 700;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: .375rem;
}
.badge-pastel-violet {
    background-color: #ede9fe !important;
    color: #6d28d9 !important;
    border: 1px solid #ddd6fe !important;
    padding: 0.35em 0.65em;
    font-size: .75em;
    font-weight: 700;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: .375rem;
}
.badge-pastel-brown {
    background-color: #f5ebe0 !important;
    color: #854d0e !important;
    border: 1px solid #e6ccb2 !important;
    padding: 0.35em 0.65em;
    font-size: .75em;
    font-weight: 700;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: .375rem;
}
.badge-pastel-blue {
    background-color: #dbeafe !important;
    color: #1d4ed8 !important;
    border: 1px solid #bfdbfe !important;
    padding: 0.35em 0.65em;
    font-size: .75em;
    font-weight: 700;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: .375rem;
}
.badge-pastel-slate {
    background-color: #e2e8f0 !important;
    color: #475569 !important;
    border: 1px solid #cbd5e1 !important;
    padding: 0.35em 0.65em;
    font-size: .75em;
    font-weight: 700;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: .375rem;
}

/* Dark Mode adaptation: low-opacity color themes to preserve accessibility and elegance */
body.dark-theme .bg-pastel-pink {
    background-color: rgba(244, 63, 94, 0.08) !important;
    border-color: rgba(244, 63, 94, 0.2) !important;
}
body.dark-theme .bg-pastel-purple {
    background-color: rgba(168, 85, 247, 0.08) !important;
    border-color: rgba(168, 85, 247, 0.2) !important;
}
body.dark-theme .bg-pastel-green {
    background-color: rgba(34, 197, 94, 0.08) !important;
    border-color: rgba(34, 197, 94, 0.2) !important;
}
body.dark-theme .bg-pastel-violet {
    background-color: rgba(139, 92, 246, 0.08) !important;
    border-color: rgba(139, 92, 246, 0.2) !important;
}
body.dark-theme .bg-pastel-brown {
    background-color: rgba(139, 90, 43, 0.08) !important;
    border-color: rgba(139, 90, 43, 0.2) !important;
}
body.dark-theme .bg-pastel-blue {
    background-color: rgba(59, 130, 246, 0.08) !important;
    border-color: rgba(59, 130, 246, 0.2) !important;
}
body.dark-theme .bg-pastel-slate {
    background-color: rgba(148, 163, 184, 0.08) !important;
    border-color: rgba(148, 163, 184, 0.2) !important;
}

/* Custom Badges Dark Mode */
body.dark-theme .badge-pastel-pink {
    background-color: rgba(244, 63, 94, 0.15) !important;
    color: #fda4af !important;
    border-color: rgba(244, 63, 94, 0.3) !important;
}
body.dark-theme .badge-pastel-purple {
    background-color: rgba(168, 85, 247, 0.15) !important;
    color: #d8b4fe !important;
    border-color: rgba(168, 85, 247, 0.3) !important;
}
body.dark-theme .badge-pastel-green {
    background-color: rgba(34, 197, 94, 0.15) !important;
    color: #86efac !important;
    border-color: rgba(34, 197, 94, 0.3) !important;
}
body.dark-theme .badge-pastel-violet {
    background-color: rgba(139, 92, 246, 0.15) !important;
    color: #c4b5fd !important;
    border-color: rgba(139, 92, 246, 0.3) !important;
}
body.dark-theme .badge-pastel-brown {
    background-color: rgba(139, 90, 43, 0.15) !important;
    color: #e6ccb2 !important;
    border-color: rgba(139, 90, 43, 0.3) !important;
}
body.dark-theme .badge-pastel-blue {
    background-color: rgba(59, 130, 246, 0.15) !important;
    color: #93c5fd !important;
    border-color: rgba(59, 130, 246, 0.3) !important;
}
body.dark-theme .badge-pastel-slate {
    background-color: rgba(148, 163, 184, 0.15) !important;
    color: #cbd5e1 !important;
    border-color: rgba(148, 163, 184, 0.3) !important;
}
</style>
