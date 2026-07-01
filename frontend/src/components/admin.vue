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
                
                <div class="row g-4">
                    <!-- Main Dashboard Column -->
                    <div class="col-lg-9 col-12">
                        <!-- Summary Stats Cards Section -->
                        <div class="row g-4 mb-4">
                            <div class="col-md-4 col-sm-6">
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
                            <div class="col-md-4 col-sm-6">
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
                            <div class="col-md-4 col-sm-12">
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

                        <!-- Graphical Analytics Row: Department Loads & Appointments Status -->
                        <div class="row g-4 mb-4">
                            <!-- Department Loads Chart -->
                            <div class="col-xl-7 col-12">
                                <div class="card shadow-sm border-0 h-100">
                                    <div class="card-header bg-white py-3 border-bottom d-flex align-items-center justify-content-between">
                                        <div class="d-flex align-items-center gap-2">
                                            <i class="bi bi-bar-chart-line text-primary fs-5"></i>
                                            <h5 class="mb-0 fw-bold text-dark">Department Loads</h5>
                                        </div>
                                        <span class="badge bg-primary-light text-primary px-3 py-2 rounded-pill font-heading">Chart.js</span>
                                    </div>
                                    <div class="card-body p-4 bg-white">
                                        <div style="width: 100%; height: 260px;" class="position-relative">
                                            <canvas id="deptLoadChart"></canvas>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Appointments Status Chart -->
                            <div class="col-xl-5 col-12">
                                <div class="card shadow-sm border-0 h-100">
                                    <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
                                        <i class="bi bi-pie-chart text-primary fs-5"></i>
                                        <h5 class="mb-0 fw-bold text-dark">Appointment Status</h5>
                                    </div>
                                    <div class="card-body d-flex flex-column align-items-center justify-content-center p-4 bg-white">
                                        <div style="width: 100%; max-width: 180px; height: 180px;" class="position-relative">
                                            <canvas id="appointmentsChart"></canvas>
                                        </div>
                                        <div class="mt-3 w-100 d-flex flex-column gap-2 text-muted small">
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

                        <!-- Appointments Records Table Row -->
                        <div class="row g-4 mb-4">
                            <div class="col-12">
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
                        </div>


                    </div>

                    <!-- Right Column: Quick Actions Sidebar -->
                    <div class="col-lg-3 col-12">


                        <!-- Quick Actions List Card -->
                        <div class="card shadow-sm border-0 quick-actions-sidebar sticky-top" style="top: 24px; z-index: 5;">
                            <div class="card-header bg-white py-3 border-bottom">
                                <h5 class="mb-0 fw-bold text-dark d-flex align-items-center gap-2">
                                    <i class="bi bi-lightning-charge-fill text-warning fs-5"></i>
                                    <span>Quick Actions</span>
                                </h5>
                            </div>
                            <div class="card-body p-4 bg-white">
                                <div class="d-flex flex-column gap-3">
                                    <button class="btn btn-quick-action action-register d-flex align-items-center gap-3 w-100 text-start" @click="openAddDoctorModal">
                                        <div class="quick-action-icon bg-primary-light text-primary">
                                            <i class="bi bi-person-plus-fill fs-5"></i>
                                        </div>
                                        <div>
                                            <strong class="d-block text-dark">Register Doctor</strong>
                                            <span class="text-muted small">Add new doctor profile</span>
                                        </div>
                                    </button>
                                    
                                    <button class="btn btn-quick-action action-manage d-flex align-items-center gap-3 w-100 text-start" @click="currentTab = 'patients'">
                                        <div class="quick-action-icon bg-success-subtle text-success">
                                            <i class="bi bi-people-fill fs-5"></i>
                                        </div>
                                        <div>
                                            <strong class="d-block text-dark">Manage Users</strong>
                                            <span class="text-muted small">Manage hospital accounts</span>
                                        </div>
                                    </button>
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
                <!-- Clean Minimalist Header & Add Button -->
                <div class="doc-sub-nav d-flex align-items-center justify-content-between mb-4 border-bottom pb-3">
                    <div>
                        <h4 class="fw-extrabold text-dark mb-1">Doctor's Dashboard</h4>
                        <p class="text-muted small mb-0"><i class="bi bi-info-circle me-1"></i>Manage schedules</p>
                    </div>
                    <button class="btn btn-primary shadow-sm rounded-pill px-4 py-2" @click="openAddDoctorModal">
                        <i class="bi bi-person-plus-fill me-2"></i>Register New Doctor
                    </button>
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
                                <span :class="['doctor-badge-status', doc.status === 'Active' ? 'active' : 'inactive']"></span>
                            </div>
                            <div class="overflow-hidden w-100">
                                <strong class="text-dark d-block text-truncate fs-5" style="font-weight: 700 !important;">{{ doc.name }}</strong>
                            </div>
                        </div>

                        <div class="d-flex align-items-center justify-content-between mb-3 px-3">
                            <span class="badge" :class="getDeptBadgeClass(doc.department)">{{ doc.department }}</span>
                            <div class="d-flex align-items-center gap-1.5">
                                <span :class="['badge rounded-pill px-2.5 py-1 text-uppercase fw-bold', doc.status === 'Active' ? 'bg-success-subtle text-success border border-success-subtle' : 'bg-secondary-subtle text-secondary border border-secondary-subtle']" style="font-size: 10px !important; margin-right: 4px;">
                                    {{ doc.status }}
                                </span>
                            </div>
                        </div>

                        <!-- Details section -->
                        <div class="doctor-schedule-section">
                            <!-- Specialization -->
                            <div class="schedule-item">
                                <span class="text-muted">{{ doc.specialization || 'General Practitioner' }}</span>
                            </div>
                            <!-- Email -->
                            <div class="schedule-item">
                                <span class="text-muted text-truncate d-block">{{ doc.email }}</span>
                            </div>
                            <!-- Contact Phone -->
                            <div class="schedule-item">
                                <span class="fw-medium text-dark">{{ doc.contact || 'No contact phone' }}</span>
                            </div>
                            <!-- Working hours -->
                            <div class="schedule-item">
                                <span class="text-muted">{{ doc.time_availability || 'Not Set' }} ({{ doc.availability }})</span>
                            </div>
                            <!-- Consultation Fee -->
                            <div class="schedule-item">
                                <span class="fw-bold text-success">₹{{ doc.consultation_fee ? doc.consultation_fee.toFixed(2) : '50.00' }}</span>
                            </div>
                        </div>

                        <!-- Card Action buttons at bottom -->
                        <div class="doctor-card-actions justify-content-between px-3 pb-3 pt-0 border-0 bg-transparent">
                            <button class="btn btn-sm btn-outline-primary rounded-pill px-3 py-1.5 fw-bold" @click="openEditDoctorModal(doc)">
                                 <i class="bi bi-pencil-fill me-1"></i>Edit Details
                            </button>
                            <div class="d-flex gap-2">
                                <button class="btn btn-sm btn-outline-secondary rounded-circle" @click="deactivateDoctor(doc)" title="Deactivate Doctor" style="width: 32px; height: 32px; padding: 0; display: inline-flex; align-items: center; justify-content: center;">
                                     <i class="bi bi-person-x-fill"></i>
                                </button>
                                <button class="btn btn-sm btn-outline-danger rounded-circle" @click="deleteDoctorPermanently(doc)" title="Delete Profile" style="width: 32px; height: 32px; padding: 0; display: inline-flex; align-items: center; justify-content: center;">
                                     <i class="bi bi-trash3-fill"></i>
                                </button>
                            </div>
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
                                        <th>Doctor Profile</th>
                                        <th>Department / Spec</th>
                                        <th>Contact Info</th>
                                        <th>Availability</th>
                                        <th>Status</th>
                                        <th class="text-end">Actions</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="doc in filteredDoctors" :key="doc.id" class="align-middle">
                                        <td class="fw-bold text-muted">#{{ doc.id }}</td>
                                        <td>
                                            <div class="d-flex align-items-center gap-2">
                                                <div class="bg-light text-primary rounded-circle d-flex align-items-center justify-content-center" style="width: 34px; height: 34px;">
                                                    <i class="bi bi-person"></i>
                                                </div>
                                                <div>
                                                    <strong class="text-dark d-block" style="font-weight: 700 !important;">{{ doc.name }}</strong>
                                                </div>
                                            </div>
                                        </td>
                                        <td>
                                            <span class="badge" :class="getDeptBadgeClass(doc.department)">{{ doc.department }}</span>
                                            <span class="text-muted small d-block">{{ doc.specialization || 'General Practitioner' }}</span>
                                        </td>
                                        <td>
                                            <span class="text-dark small d-block"><i class="bi bi-envelope text-muted me-1"></i>{{ doc.email }}</span>
                                            <span class="text-muted small d-block"><i class="bi bi-telephone text-muted me-1"></i>{{ doc.contact || 'No contact phone' }}</span>
                                        </td>
                                        <td>
                                            <span class="text-muted small d-block"><i class="bi bi-clock me-1"></i>{{ doc.time_availability || 'Not Set' }}</span>
                                            <span class="text-dark small d-block">({{ doc.availability }})</span>
                                        </td>
                                        <td>
                                            <div class="d-flex align-items-center gap-2">
                                                <span :class="['badge rounded-pill px-2.5 py-1 text-uppercase fw-bold', doc.status === 'Active' ? 'bg-success-subtle text-success border border-success-subtle' : 'bg-secondary-subtle text-secondary border border-secondary-subtle']" style="font-size: 10px !important;">
                                                    {{ doc.status }}
                                                </span>
                                            </div>
                                        </td>
                                        <td class="text-end">
                                            <div class="d-flex justify-content-end gap-2">
                                                 <button class="btn btn-sm btn-outline-primary rounded-pill px-2.5 py-1 fw-bold" @click="openEditDoctorModal(doc)">
                                                     <i class="bi bi-pencil-fill me-1"></i>Edit Details
                                                 </button>
                                                 <button class="btn-action-circle warning" @click="deactivateDoctor(doc)" title="Deactivate Doctor">
                                                     <i class="bi bi-person-x-fill"></i>
                                                 </button>
                                                 <button class="btn-action-circle danger" @click="deleteDoctorPermanently(doc)" title="Delete Profile">
                                                     <i class="bi bi-trash3-fill"></i>
                                                 </button>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr v-if="filteredDoctors.length === 0">
                                        <td colspan="7" class="text-center text-muted py-5">
                                            <i class="bi bi-folder-x fs-3 d-block mb-2"></i>
                                            No doctors found matching the search query.
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
                <!-- Unified Control Bar for Patients -->
                <div class="card shadow-sm border-0 mb-4 bg-pastel-slate">
                    <div class="card-body p-4 d-flex flex-column flex-md-row align-items-center justify-content-between gap-3">
                        <!-- Gentle Stylized Search Bar -->
                        <div class="w-100 flex-grow-1" style="max-width: 500px;">
                            <div class="input-group search-bar-premium shadow-sm">
                                <span class="input-group-text bg-transparent border-end-0"><i class="bi bi-search text-muted"></i></span>
                                <input type="text" class="form-control border-start-0 border-end-0" v-model="searchPatQuery" placeholder="Search patients by contact, name, email or ID..." @keyup.enter="searchPatients">
                                <button v-if="searchPatQuery" class="btn btn-link text-muted border-start-0 border-end-0" @click="patSearchResults = []; searchPatQuery = ''" style="background: transparent; z-index: 10;">
                                    <i class="bi bi-x-circle-fill"></i>
                                </button>
                                <button class="btn btn-primary px-4 fw-bold" @click="searchPatients">Search DB</button>
                            </div>
                        </div>

                        <!-- Gentle Stylized Dropdown Filter -->
                        <div class="d-flex align-items-center gap-3 w-100 w-md-auto justify-content-between">
                            <div class="d-flex align-items-center gap-2">
                                <label class="mb-0 small fw-bold text-muted text-uppercase tracking-wider">Filter Visits:</label>
                                <select class="form-select w-auto bg-light border-1 shadow-sm font-semibold" v-model="patientFilter">
                                    <option value="All">All Patients</option>
                                    <option value="Recent">Recent Appointments (Last 30 days)</option>
                                    <option value="Upcoming">Upcoming Scheduled Bookings</option>
                                    <option value="None">No Appointments Logged</option>
                                </select>
                            </div>
                            <div class="btn-group view-switcher-group shadow-sm p-1 rounded-3 bg-light border" role="group">
                                <button class="btn btn-sm btn-view-mode" :class="{ active: patientViewMode === 'grid' }" @click="patientViewMode = 'grid'">
                                    <i class="bi bi-grid-fill"></i>
                                </button>
                                <button class="btn btn-sm btn-view-mode" :class="{ active: patientViewMode === 'table' }" @click="patientViewMode = 'table'">
                                    <i class="bi bi-list-task"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Server Search results alert indicator -->
                <div v-if="patSearchResults.length" class="alert alert-info border-0 shadow-sm d-flex justify-content-between align-items-center mb-4">
                    <div>
                        <i class="bi bi-search me-2 fs-5"></i>
                        <span>Found <strong>{{ patSearchResults.length }}</strong> match(es) from server database.</span>
                    </div>
                    <button class="btn btn-sm btn-outline-info text-dark" @click="patSearchResults = []; searchPatQuery = ''">Reset Search</button>
                </div>

                <!-- View 1: Card-Based Directory Grid -->
                <div v-if="patientViewMode === 'grid'" class="doctor-card-grid fade-in-up">
                    <div v-for="pat in filteredPatients" :key="pat.id" class="doctor-profile-card shadow-sm border-0 h-100 bg-pastel-blue">
                        <!-- Top Info Header -->
                        <div class="doctor-card-header">
                            <div class="doctor-avatar-wrapper">
                                <div class="doctor-card-avatar" style="background-color: var(--theme-primary) !important; color: white !important;">
                                    {{ pat.name ? pat.name.split(' ').pop().charAt(0).toUpperCase() : 'P' }}
                                </div>
                            </div>
                            <div class="overflow-hidden w-100">
                                <strong class="text-dark d-block text-truncate fs-5" style="font-weight: 700 !important;">{{ pat.name }}</strong>
                                <span class="text-muted small d-block">PID: #{{ pat.id }} • User: {{ pat.user_id }}</span>
                            </div>
                        </div>

                        <!-- Info details -->
                        <div class="doctor-schedule-section">
                            <!-- Email -->
                            <div class="schedule-item">
                                <i class="bi bi-envelope text-primary"></i>
                                <span class="text-muted text-truncate">{{ pat.email }}</span>
                            </div>
                            <!-- Contact Number -->
                            <div class="schedule-item">
                                <i class="bi bi-telephone text-primary"></i>
                                <span class="fw-medium text-dark">{{ pat.contact || 'No contact phone' }}</span>
                            </div>
                            <!-- Registration Date -->
                            <div class="schedule-item">
                                <i class="bi bi-calendar-event text-primary"></i>
                                <span class="text-muted small">Registered: {{ pat.registration_date }}</span>
                            </div>
                            <!-- Home Address -->
                            <div class="schedule-item">
                                <i class="bi bi-geo-alt text-primary"></i>
                                <span class="text-muted text-truncate d-block">{{ pat.address || 'Address not registered' }}</span>
                            </div>
                        </div>

                        <!-- Appointments Quick Stats Badging -->
                        <div class="px-3 mb-3 d-flex align-items-center gap-2">
                            <span class="badge bg-primary rounded-pill px-2.5 py-1 fw-bold" style="font-size: 11px !important;">
                                <i class="bi bi-calendar-check me-1"></i>{{ pat.total_appointments }} Visits Logged
                            </span>
                            <span v-if="pat.has_upcoming" class="badge bg-success-subtle text-success border border-success-subtle rounded-pill px-2.5 py-1 fw-bold" style="font-size: 11px !important;">
                                Upcoming Scheduled
                            </span>
                        </div>

                        <!-- Card Actions -->
                        <div class="doctor-card-actions">
                            <button class="btn-action-circle success" @click="openViewPatientModal(pat)" title="View Medical Dossier">
                                 <i class="bi bi-file-medical-fill"></i>
                            </button>
                            <button class="btn-action-circle primary" @click="openEditPatientModal(pat)" title="Edit Contact details">
                                 <i class="bi bi-pencil-fill"></i>
                            </button>
                            <button class="btn-action-circle danger" @click="removeUser(pat.user_id)" title="Remove Patient Profile">
                                 <i class="bi bi-trash3-fill"></i>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- View 2: Compact List/Table View -->
                <div v-if="patientViewMode === 'table'" class="card shadow-sm border-0 fade-in-up bg-pastel-slate">
                    <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
                        <i class="bi bi-list-stars text-primary fs-5"></i>
                        <h5 class="mb-0 fw-bold text-dark">Registered Patients List</h5>
                    </div>
                    <div class="card-body p-0">
                        <div class="table-responsive border-0">
                            <table class="table table-hover table-striped mb-0">
                                <thead>
                                    <tr>
                                        <th style="width: 80px;">PID</th>
                                        <th>Patient Info</th>
                                        <th>Contact Phone</th>
                                        <th>Registration Date</th>
                                        <th>Total Bookings</th>
                                        <th>Next Action</th>
                                        <th class="text-end">Actions</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="pat in filteredPatients" :key="pat.id" class="align-middle">
                                        <td class="fw-bold text-muted">#{{ pat.id }}</td>
                                        <td>
                                            <div class="d-flex align-items-center gap-2">
                                                <div class="bg-light text-primary rounded-circle d-flex align-items-center justify-content-center" style="width: 34px; height: 34px;">
                                                    <i class="bi bi-person"></i>
                                                </div>
                                                <div>
                                                    <strong class="text-dark d-block" style="font-weight: 700 !important;">{{ pat.name }}</strong>
                                                    <span class="text-muted small">User ID: {{ pat.user_id }} • {{ pat.email }}</span>
                                                </div>
                                            </div>
                                        </td>
                                        <td>
                                            <span class="text-dark small"><i class="bi bi-telephone text-muted me-1"></i>{{ pat.contact || 'N/A' }}</span>
                                            <span class="text-muted small d-block"><i class="bi bi-geo-alt me-1"></i>{{ pat.address || 'N/A' }}</span>
                                        </td>
                                        <td><span class="text-muted small">{{ pat.registration_date }}</span></td>
                                        <td>
                                            <span class="badge bg-light text-dark border rounded-pill px-3 py-1">{{ pat.total_appointments }} visits</span>
                                        </td>
                                        <td>
                                            <span v-if="pat.has_upcoming" class="badge bg-success-subtle text-success border border-success-subtle rounded-pill px-2.5 py-1 fw-bold" style="font-size: 10px !important;">
                                                Upcoming Booking
                                            </span>
                                            <span v-else class="text-muted small">-</span>
                                        </td>
                                        <td class="text-end">
                                            <div class="d-flex justify-content-end gap-2">
                                                 <button class="btn-action-circle success" @click="openViewPatientModal(pat)" title="View Medical Dossier">
                                                     <i class="bi bi-file-medical-fill"></i>
                                                 </button>
                                                 <button class="btn-action-circle primary" @click="openEditPatientModal(pat)" title="Edit Contact details">
                                                     <i class="bi bi-pencil-fill"></i>
                                                 </button>
                                                 <button class="btn-action-circle danger" @click="removeUser(pat.user_id)" title="Remove Patient Profile">
                                                     <i class="bi bi-trash3-fill"></i>
                                                 </button>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr v-if="filteredPatients.length === 0">
                                        <td colspan="7" class="text-center text-muted py-5">
                                            <i class="bi bi-folder-x fs-3 d-block mb-2"></i>
                                            No patients found matching the search or filter query.
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

        <!-- =========================================
             AESTHETIC GLASSMORPHIC MODALS CONTAINER
        ========================================== -->
        <!-- Modal 1: Add Doctor -->
        <div class="glass-modal-overlay" v-if="activeModal === 'addDoctor'" @click.self="closeModal">
            <div class="glass-modal-container">
                <div class="glass-modal-header bg-pastel-blue">
                    <h5 class="glass-modal-title text-dark"><i class="bi bi-person-plus-fill me-2 text-primary"></i>Register New Doctor</h5>
                    <button class="glass-modal-close-btn" @click="closeModal"><i class="bi bi-x-lg"></i></button>
                </div>
                <form @submit.prevent="submitAddDoctor">
                    <div class="glass-modal-body">
                        <div class="row g-3">
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-secondary">Doctor Name</label>
                                <input type="text" class="form-control" v-model="newDoctor.name" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-secondary">Email Address</label>
                                <input type="email" class="form-control" v-model="newDoctor.email" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-secondary">Phone Number</label>
                                <input type="text" class="form-control" v-model="newDoctor.contact">
                            </div>
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-secondary">Specialization</label>
                                <input type="text" class="form-control" v-model="newDoctor.specialization" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-secondary">Department</label>
                                <select class="form-select" v-model="newDoctor.department_name" required>
                                    <option value="General Medicine">General Medicine</option>
                                    <option value="Cardiology">Cardiology</option>
                                    <option value="Neurology">Neurology</option>
                                    <option value="Dermatology">Dermatology</option>
                                    <option value="Pediatrics">Pediatrics</option>
                                    <option value="Dentistry">Dentistry</option>
                                </select>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-secondary">Consultation Fee (₹)</label>
                                <input type="number" step="0.01" min="0" class="form-control" v-model="newDoctor.consultation_fee" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-secondary">Working Days</label>
                                <select class="form-select" v-model="newDoctor.availability" required>
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
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-secondary">Working Hours</label>
                                <input type="text" class="form-control" v-model="newDoctor.time_availability" required>
                            </div>
                            <div class="col-12">
                                <label class="form-label small fw-bold text-secondary">Password (optional)</label>
                                <input type="text" class="form-control" v-model="newDoctor.password">
                            </div>
                        </div>
                    </div>
                    <div class="glass-modal-footer">
                        <button type="button" class="btn btn-outline-secondary rounded-pill px-4" @click="closeModal">Cancel</button>
                        <button type="submit" class="btn btn-primary rounded-pill px-4">Register Doctor</button>
                    </div>
                </form>
            </div>
        </div>

        <!-- Modal 2: Edit Doctor -->
        <div class="glass-modal-overlay" v-if="activeModal === 'editDoctor'" @click.self="closeModal">
            <div class="glass-modal-container">
                <div class="glass-modal-header bg-pastel-blue">
                    <h5 class="glass-modal-title text-dark"><i class="bi bi-pencil-square me-2 text-primary"></i>Edit Doctor Details</h5>
                    <button class="glass-modal-close-btn" @click="closeModal"><i class="bi bi-x-lg"></i></button>
                </div>
                <form @submit.prevent="submitEditDoctor">
                    <div class="glass-modal-body">
                        <div class="row g-3">
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-secondary">Doctor Name</label>
                                <input type="text" class="form-control" v-model="selectedDoctor.name" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-secondary">Email Address</label>
                                <input type="email" class="form-control" v-model="selectedDoctor.email" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-secondary">Phone Number</label>
                                <input type="text" class="form-control" v-model="selectedDoctor.contact">
                            </div>
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-secondary">Specialization</label>
                                <input type="text" class="form-control" v-model="selectedDoctor.specialization" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-secondary">Department</label>
                                <select class="form-select" v-model="selectedDoctor.department" required>
                                    <option value="General Medicine">General Medicine</option>
                                    <option value="Cardiology">Cardiology</option>
                                    <option value="Neurology">Neurology</option>
                                    <option value="Dermatology">Dermatology</option>
                                    <option value="Pediatrics">Pediatrics</option>
                                    <option value="Dentistry">Dentistry</option>
                                </select>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-secondary">Consultation Fee (₹)</label>
                                <input type="number" step="0.01" min="0" class="form-control" v-model="selectedDoctor.consultation_fee" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-secondary">Working Days</label>
                                <select class="form-select" v-model="selectedDoctor.availability" required>
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
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-secondary">Working Hours</label>
                                <input type="text" class="form-control" v-model="selectedDoctor.time_availability" required>
                            </div>
                            <div class="col-12">
                                <label class="form-label small fw-bold text-secondary">Roster Status</label>
                                <select class="form-select" v-model="selectedDoctor.status" required>
                                    <option value="Active">Active / On Duty</option>
                                    <option value="Unavailable">Unavailable / Off Duty</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="glass-modal-footer">
                        <button type="button" class="btn btn-outline-secondary rounded-pill px-4" @click="closeModal">Cancel</button>
                        <button type="submit" class="btn btn-primary rounded-pill px-4">Save Changes</button>
                    </div>
                </form>
            </div>
        </div>

        <!-- Modal 3: View Patient Details Dossier -->
        <div class="glass-modal-overlay" v-if="activeModal === 'viewPatient'" @click.self="closeModal">
            <div class="glass-modal-container wide">
                <div class="glass-modal-header bg-pastel-blue">
                    <h5 class="glass-modal-title text-dark"><i class="bi bi-file-medical-fill me-2 text-primary"></i>Patient Health Dossier</h5>
                    <button class="glass-modal-close-btn" @click="closeModal"><i class="bi bi-x-lg"></i></button>
                </div>
                <div class="glass-modal-body bg-light">
                    <!-- Patient Quick Info Header Card -->
                    <div class="card shadow-sm border-0 mb-4 p-4 bg-white rounded-4">
                        <div class="row align-items-center">
                            <div class="col-md-8">
                                <h3 class="fw-bold mb-1 font-heading text-dark">{{ patientDetail.name }}</h3>
                                <p class="text-muted small mb-3">PID: #{{ patientDetail.id }} • Registered on {{ patientDetail.registration_date }}</p>
                                <div class="row g-3">
                                    <div class="col-sm-6 small"><i class="bi bi-envelope text-muted me-2"></i>{{ patientDetail.email }}</div>
                                    <div class="col-sm-6 small"><i class="bi bi-telephone text-muted me-2"></i>{{ patientDetail.contact || 'No contact phone' }}</div>
                                    <div class="col-12 small"><i class="bi bi-geo-alt text-muted me-2"></i>{{ patientDetail.address || 'Address not registered' }}</div>
                                </div>
                            </div>
                            <div class="col-md-4 text-md-end mt-3 mt-md-0">
                                <button class="btn btn-outline-primary rounded-pill w-100 py-2.5 shadow-sm fw-bold" @click="downloadPatientReport(patientDetail.id, patientDetail.name)">
                                    <i class="bi bi-file-earmark-pdf me-2"></i>Download PDF Report
                                </button>
                            </div>
                        </div>
                    </div>

                    <!-- Upcoming Appointments -->
                    <div class="card shadow-sm border-0 mb-4 bg-white">
                        <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
                            <i class="bi bi-calendar-event text-primary fs-5"></i>
                            <h5 class="mb-0 fw-bold text-dark">Upcoming Appointments</h5>
                        </div>
                        <div class="card-body p-0">
                            <div class="table-responsive border-0">
                                <table class="table table-hover table-striped mb-0">
                                    <thead>
                                        <tr>
                                            <th>Doctor Name</th>
                                            <th>Spec</th>
                                            <th>Date</th>
                                            <th>Time Slot</th>
                                            <th>Status</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="appt in patientDetail.upcoming" :key="appt.id" class="align-middle">
                                            <td class="fw-bold">{{ appt.doctor_name }}</td>
                                            <td>{{ appt.specialization }}</td>
                                            <td><i class="bi bi-calendar3 me-1 text-muted"></i>{{ appt.date }}</td>
                                            <td><span class="badge bg-secondary rounded-pill px-3 py-1.5">{{ appt.time_slot }}</span></td>
                                            <td>
                                                <span class="badge rounded-pill bg-primary-subtle text-primary border border-primary-subtle px-2.5 py-1">
                                                    {{ appt.status }}
                                                </span>
                                            </td>
                                        </tr>
                                        <tr v-if="!patientDetail.upcoming || patientDetail.upcoming.length === 0">
                                            <td colspan="5" class="text-center py-4 text-muted small">No upcoming appointments.</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>

                    <!-- Appointment History & Medical Notes -->
                    <div class="card shadow-sm border-0 mb-0 bg-white">
                        <div class="card-header bg-white py-3 border-bottom d-flex align-items-center gap-2">
                            <i class="bi bi-clock-history text-primary fs-5"></i>
                            <h5 class="mb-0 fw-bold text-dark">Medical Consultation History</h5>
                        </div>
                        <div class="card-body p-0">
                            <div class="table-responsive border-0">
                                <table class="table table-hover table-striped mb-0">
                                    <thead>
                                        <tr>
                                            <th>Consultant</th>
                                            <th>Date</th>
                                            <th>Status</th>
                                            <th>Diagnosis & Prescriptions</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="appt in patientDetail.history" :key="appt.id" class="align-middle">
                                            <td>
                                                <strong class="d-block">{{ appt.doctor_name }}</strong>
                                                <small class="text-muted">{{ appt.specialization }}</small>
                                            </td>
                                            <td>{{ appt.date }}</td>
                                            <td>
                                                <span :class="['badge rounded-pill', appt.status === 'Completed' ? 'bg-success-subtle text-success border border-success-subtle' : 'bg-warning-subtle text-warning border border-warning-subtle']">
                                                    {{ appt.status }}
                                                </span>
                                            </td>
                                            <td>
                                                <div class="p-2.5 rounded-3 bg-light text-muted small" style="max-width: 380px;">
                                                    <div v-if="appt.diagnosis"><strong>Diagnosis:</strong> {{ appt.diagnosis }}</div>
                                                    <div v-if="appt.prescription" class="mt-1"><strong>Prescription:</strong> {{ appt.prescription }}</div>
                                                    <div v-if="appt.notes" class="mt-1"><strong>Notes:</strong> {{ appt.notes }}</div>
                                                    <span v-if="!appt.diagnosis && !appt.prescription && !appt.notes" class="text-muted italic">No diagnosis records found</span>
                                                </div>
                                            </td>
                                        </tr>
                                        <tr v-if="!patientDetail.history || patientDetail.history.length === 0">
                                            <td colspan="4" class="text-center py-4 text-muted small">No past consultation history records.</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="glass-modal-footer">
                    <button type="button" class="btn btn-secondary rounded-pill px-5" @click="closeModal">Close Dossier</button>
                </div>
            </div>
        </div>

        <!-- Modal 4: Edit Patient Contact Info -->
        <div class="glass-modal-overlay" v-if="activeModal === 'editPatient'" @click.self="closeModal">
            <div class="glass-modal-container">
                <div class="glass-modal-header bg-pastel-blue">
                    <h5 class="glass-modal-title text-dark"><i class="bi bi-pencil-square me-2 text-primary"></i>Edit Patient Contact</h5>
                    <button class="glass-modal-close-btn" @click="closeModal"><i class="bi bi-x-lg"></i></button>
                </div>
                <form @submit.prevent="submitEditPatient">
                    <div class="glass-modal-body">
                        <div class="row g-3">
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-secondary">Full Name</label>
                                <input type="text" class="form-control" v-model="selectedPatient.name" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-secondary">Email Address</label>
                                <input type="email" class="form-control" v-model="selectedPatient.email" required>
                            </div>
                            <div class="col-12">
                                <label class="form-label small fw-bold text-secondary">Contact Number</label>
                                <input type="text" class="form-control" v-model="selectedPatient.contact" required>
                            </div>
                            <div class="col-12">
                                <label class="form-label small fw-bold text-secondary">Home Address</label>
                                <textarea class="form-control" v-model="selectedPatient.address" rows="3"></textarea>
                            </div>
                        </div>
                    </div>
                    <div class="glass-modal-footer">
                        <button type="button" class="btn btn-outline-secondary rounded-pill px-4" @click="closeModal">Cancel</button>
                        <button type="submit" class="btn btn-primary rounded-pill px-4">Save Contact</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            currentTab: 'overview',
            token: localStorage.getItem('access_token'),
            error: '', success: '',
            stats: { total_patients: 0, total_doctors: 0, total_appointments: 0, total_revenue: 0, monthly_trends: [], monthly_revenue: [], daily_volumes: [] },
            appointments: [],
            doctors: [],
            appointmentFilter: 'Booked',
            searchDocQuery: '', docSearchResults: [],
            searchPatQuery: '', patSearchResults: [],
            patients: [],
            showPassword: false,
            chartInstance: null,
            deptLoadChartInstance: null,
            isDarkMode: false,
            viewMode: 'grid',
            patientViewMode: 'grid',
            selectedDeptFilter: 'All',
            departments: ['All', 'General Medicine', 'Cardiology', 'Neurology', 'Dermatology', 'Pediatrics', 'Dentistry'],
            
            // New Modals and Data State properties
            activeModal: null,
            selectedDoctor: { id: null, name: '', email: '', contact: '', specialization: '', department: 'General Medicine', availability: 'Everyday', time_availability: '10:00 AM - 09:00 PM', consultation_fee: 50.0, status: 'Active' },
            selectedPatient: { id: null, name: '', email: '', contact: '', address: '' },
            patientDetail: { id: null, name: '', email: '', contact: '', address: '', registration_date: '', total_appointments: 0, history: [], upcoming: [] },
            patientFilter: 'All',
            newDoctor: { name: '', email: '', password: '', specialization: '', department_name: 'General Medicine', availability: 'Everyday', time_availability: '', consultation_fee: '', contact: '' }
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
                const patientsData = await res4.json();
                this.patients = patientsData.map(p => ({ ...p, isEditing: false }));

                this.$nextTick(() => {
                    this.renderChart();
                });
            } catch (e) { this.showMsg('error', "Loading data..."); } 
        },

        renderChart() {
            // Render Appointment Status Doughnut Chart
            const ctx = document.getElementById('appointmentsChart');
            if (ctx) {
                const booked = this.appointments.filter(a => a.status === 'Booked').length;
                const completed = this.appointments.filter(a => a.status === 'Completed').length;
                const cancelled = this.appointments.filter(a => a.status === 'Cancelled').length;
                
                if (this.chartInstance) {
                    this.chartInstance.data.datasets[0].data = [booked, completed, cancelled];
                    this.chartInstance.update();
                } else {
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
                                legend: { display: false }
                            },
                            cutout: '75%'
                        }
                    });
                }
            }

            // Render Department Loads Chart
            const ctxDept = document.getElementById('deptLoadChart');
            if (ctxDept) {
                const depts = this.departments.filter(d => d !== 'All');
                const deptLoadData = depts.map(dept => {
                    const docCount = this.doctors.filter(d => d.department === dept).length;
                    const apptCount = this.appointments.filter(a => {
                        const doc = this.doctors.find(d => d.name === a.doctor);
                        return doc && doc.department === dept;
                    }).length;
                    return docCount + apptCount;
                });

                if (this.deptLoadChartInstance) {
                    this.deptLoadChartInstance.data.datasets[0].data = deptLoadData;
                    this.deptLoadChartInstance.update();
                } else {
                    this.deptLoadChartInstance = new Chart(ctxDept, {
                        type: 'bar',
                        data: {
                            labels: depts,
                            datasets: [{
                                label: 'Department Load (Doctors + Appointments)',
                                data: deptLoadData,
                                backgroundColor: 'rgba(99, 102, 241, 0.85)',
                                hoverBackgroundColor: 'rgba(79, 70, 229, 1)',
                                borderRadius: 8,
                                borderWidth: 0
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            plugins: {
                                legend: { display: false },
                                tooltip: {
                                    callbacks: {
                                        label: function(context) {
                                            return ` Load Factor: ${context.raw}`;
                                        }
                                    }
                                }
                            },
                            scales: {
                                x: {
                                    grid: { display: false }
                                },
                                y: {
                                    beginAtZero: true,
                                    ticks: { stepSize: 1 },
                                    grid: { color: 'rgba(0, 0, 0, 0.05)' }
                                }
                            }
                        }
                    });
                }
            }
        },

        // Modal triggers and management methods
        openAddDoctorModal() {
            this.newDoctor = { name: '', email: '', password: '', specialization: '', department_name: 'General Medicine', availability: 'Everyday', time_availability: '', consultation_fee: '', contact: '' };
            this.activeModal = 'addDoctor';
        },

        openEditDoctorModal(doc) {
            this.selectedDoctor = {
                id: doc.id,
                name: doc.name,
                email: doc.email,
                contact: doc.contact,
                specialization: doc.specialization,
                department: doc.department === 'N/A' ? 'General Medicine' : doc.department,
                availability: doc.availability || 'Everyday',
                time_availability: doc.time_availability || '10:00 AM - 09:00 PM',
                consultation_fee: doc.consultation_fee || 50.0,
                status: doc.status || 'Active'
            };
            this.activeModal = 'editDoctor';
        },

        openEditPatientModal(pat) {
            this.selectedPatient = {
                id: pat.id,
                name: pat.name,
                email: pat.email,
                contact: pat.contact,
                address: pat.address
            };
            this.activeModal = 'editPatient';
        },

        async openViewPatientModal(pat) {
            try {
                const res = await fetch('http://127.0.0.1:5000/api/admin/patients/' + pat.id, { headers: this.authHeader() });
                if (res.ok) {
                    const detail = await res.json();
                    // Fetch specific booking history from dedicated history endpoint
                    const resHistory = await fetch('http://127.0.0.1:5000/api/admin/patients/' + pat.id + '/history', { headers: this.authHeader() });
                    if (resHistory.ok) {
                        const historyData = await resHistory.json();
                        detail.history = historyData.history;
                        detail.upcoming = historyData.upcoming;
                    }
                    this.patientDetail = detail;
                    this.activeModal = 'viewPatient';
                } else {
                    this.showMsg('error', 'Failed to retrieve patient health dossier.');
                }
            } catch (e) {
                this.showMsg('error', 'Network error retrieving dossier.');
            }
        },

        async toggleDoctorStatus(doc) {
            try {
                const newStatus = doc.status === 'Active' ? 'Unavailable' : 'Active';
                const payload = { status: newStatus };
                const res = await fetch('http://127.0.0.1:5000/api/admin/doctors/' + doc.id, {
                    method: 'PUT',
                    headers: this.authHeader(),
                    body: JSON.stringify(payload)
                });
                if (res.ok) {
                    this.showMsg('success', `Doctor status updated to ${newStatus}.`);
                    this.fetchData();
                } else {
                    this.showMsg('error', 'Failed to update doctor status.');
                }
            } catch (e) {
                this.showMsg('error', 'Network error updating doctor status.');
            }
        },

        closeModal() {
            this.activeModal = null;
        },

        async submitAddDoctor() {
            try {
                const payload = {
                    username: this.newDoctor.name,
                    email: this.newDoctor.email,
                    password: this.newDoctor.password,
                    specialization: this.newDoctor.specialization,
                    department_name: this.newDoctor.department_name,
                    availability: this.newDoctor.availability,
                    time_availability: this.newDoctor.time_availability,
                    consultation_fee: parseFloat(this.newDoctor.consultation_fee || 50.0),
                    contact: this.newDoctor.contact
                };
                const res = await fetch('http://127.0.0.1:5000/api/admin/doctors', {
                    method: 'POST', headers: this.authHeader(), body: JSON.stringify(payload)
                });
                const data = await res.json();
                if (res.ok) {
                    this.showMsg('success', "Doctor account created successfully!");
                    alert("DOCTOR REGISTERED SUCCESSFULLY!\n\nEmail: " + payload.email + "\nGenerated Password: " + data.generated_password);
                    this.closeModal();
                    this.fetchData();
                } else {
                    this.showMsg('error', data.message || "Failed to create doctor profile.");
                }
            } catch (e) {
                this.showMsg('error', "Network error creating doctor profile.");
            }
        },

        async submitEditDoctor() {
            try {
                const payload = {
                    name: this.selectedDoctor.name,
                    email: this.selectedDoctor.email,
                    contact: this.selectedDoctor.contact,
                    specialization: this.selectedDoctor.specialization,
                    department: this.selectedDoctor.department,
                    availability: this.selectedDoctor.availability,
                    time_availability: this.selectedDoctor.time_availability,
                    consultation_fee: parseFloat(this.selectedDoctor.consultation_fee || 50.0),
                    status: this.selectedDoctor.status
                };
                const res = await fetch('http://127.0.0.1:5000/api/admin/doctors/' + this.selectedDoctor.id, {
                    method: 'PUT', headers: this.authHeader(), body: JSON.stringify(payload)
                });
                if (res.ok) {
                    this.showMsg('success', "Doctor profile updated successfully!");
                    this.closeModal();
                    this.fetchData();
                } else {
                    const data = await res.json();
                    this.showMsg('error', data.message || "Failed to save profile changes.");
                }
            } catch (e) {
                this.showMsg('error', "Network error saving doctor changes.");
            }
        },

        async submitEditPatient() {
            try {
                const res = await fetch('http://127.0.0.1:5000/api/admin/patients/' + this.selectedPatient.id, {
                    method: 'PUT', headers: this.authHeader(), body: JSON.stringify(this.selectedPatient)
                });
                if (res.ok) {
                    this.showMsg('success', "Patient contact records updated.");
                    this.closeModal();
                    this.fetchData();
                } else {
                    const data = await res.json();
                    this.showMsg('error', data.message || "Failed to update contact records.");
                }
            } catch (e) {
                this.showMsg('error', "Network error updating patient.");
            }
        },

        async deactivateDoctor(doc) {
            if (confirm(`Are you sure you want to deactivate ${doc.name}? Their profile will show as Unavailable.`)) {
                try {
                    const res = await fetch(`http://127.0.0.1:5000/api/admin/doctors/${doc.id}?action=deactivate`, {
                        method: 'DELETE', headers: this.authHeader()
                    });
                    if (res.ok) {
                        this.showMsg('success', `${doc.name} profile deactivated.`);
                        this.fetchData();
                    } else {
                        const data = await res.json();
                        this.showMsg('error', data.message);
                    }
                } catch (e) {
                    this.showMsg('error', "Network error deactivating doctor.");
                }
            }
        },

        async deleteDoctorPermanently(doc) {
            if (confirm(`DANGER: Permanently delete doctor ${doc.name} and their user login profile? This cannot be undone.`)) {
                try {
                    const res = await fetch(`http://127.0.0.1:5000/api/admin/doctors/${doc.id}?action=delete`, {
                        method: 'DELETE', headers: this.authHeader()
                    });
                    if (res.ok) {
                        this.showMsg('success', `${doc.name} profile permanently removed.`);
                        this.fetchData();
                    } else {
                        const data = await res.json();
                        this.showMsg('error', data.message);
                    }
                } catch (e) {
                    this.showMsg('error', "Network error deleting profile.");
                }
            }
        },

        async downloadPatientReport(patientId, patientName) {
            try {
                this.showMsg('success', 'Preparing PDF download...');
                const res = await fetch(`http://127.0.0.1:5000/api/admin/patients/${patientId}/export-history`, {
                    headers: this.authHeader()
                });
                if (res.ok) {
                    const blob = await res.blob();
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = `Medical_History_${patientName.replace(/\s+/g, '_')}.pdf`;
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    window.URL.revokeObjectURL(url);
                    this.showMsg('success', 'PDF Medical History Report downloaded!');
                } else {
                    this.showMsg('error', 'Failed to generate PDF history report.');
                }
            } catch (e) {
                this.showMsg('error', 'Network error preparing export PDF.');
            }
        },

        async searchDoctors() {
            if (!this.searchDocQuery) return;
            const res = await fetch('http://127.0.0.1:5000/api/admin/doctors/search?q=' + this.searchDocQuery, { headers: this.authHeader() });
            if (res.ok) {
                this.docSearchResults = await res.json();
                if (this.docSearchResults.length === 0) {
                    alert('No doctor profiles match search criteria.');
                }
            }
        },

        async searchPatients() {
            if (!this.searchPatQuery) return;
            const res = await fetch('http://127.0.0.1:5000/api/admin/patients/search?q=' + this.searchPatQuery, { headers: this.authHeader() });
            if (res.ok) {
                const results = await res.json();
                this.patSearchResults = results.map(p => ({ ...p, isEditing: false }));
                if (this.patSearchResults.length === 0) {
                    alert('No patient profiles match search criteria.');
                }
            }
        },

        async removeUser(user_id) {
            if (confirm("DANGER: Permanently remove this profile? This will delete all logins and bookings associated with this user.")) {
                const res = await fetch('http://127.0.0.1:5000/api/admin/user/' + user_id, { method: 'DELETE', headers: this.authHeader() });
                if (res.ok) {
                    this.showMsg('success', "Profile removed from the hospital records.");
                    this.fetchData();
                } else {
                    const data = await res.json();
                    this.showMsg('error', data.message);
                }
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
        },
        filteredPatients() {
            let list = this.patSearchResults.length ? this.patSearchResults : this.patients;
            
            // Filter by Appointment status
            if (this.patientFilter === 'Upcoming') {
                list = list.filter(p => p.has_upcoming);
            } else if (this.patientFilter === 'Recent') {
                list = list.filter(p => p.has_recent);
            } else if (this.patientFilter === 'None') {
                list = list.filter(p => p.total_appointments === 0);
            }

            if (this.searchPatQuery) {
                const q = this.searchPatQuery.toLowerCase();
                list = list.filter(p => 
                    (p.name && p.name.toLowerCase().includes(q)) || 
                    (p.email && p.email.toLowerCase().includes(q)) ||
                    (p.contact && p.contact.toLowerCase().includes(q)) ||
                    (p.id && p.id.toString().includes(q)) ||
                    (p.address && p.address.toLowerCase().includes(q))
                );
            }
            return list;
        }
    },
    watch: {
        currentTab(newTab) {
            if (newTab === 'overview') {
                this.$nextTick(() => {
                    this.renderChart();
                });
            }
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

/* Padding left removed for plain inputs */

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

/* Glassmorphic Modal Styling */
.glass-modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(15, 23, 42, 0.3);
    backdrop-filter: blur(12px) saturate(180%);
    -webkit-backdrop-filter: blur(12px) saturate(180%);
    z-index: 2100;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1rem;
}

.glass-modal-container {
    background: rgba(255, 255, 255, 0.75) !important;
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.45) !important;
    border-radius: var(--border-radius-lg, 24px) !important;
    box-shadow: 0 24px 64px -12px rgba(124, 115, 230, 0.18) !important;
    width: 100%;
    max-width: 600px;
    max-height: 85vh;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    animation: modalFadeInUp 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

body.dark-theme .glass-modal-container {
    background: rgba(30, 41, 59, 0.75) !important;
    border-color: rgba(255, 255, 255, 0.08) !important;
    box-shadow: 0 24px 64px -12px rgba(0, 0, 0, 0.5) !important;
}

.glass-modal-container.wide {
    max-width: 850px;
}

.glass-modal-header {
    padding: 1.5rem 2rem;
    border-bottom: 1.5px solid rgba(139, 115, 85, 0.1);
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.glass-modal-title {
    margin: 0;
    font-size: 20px !important;
    font-weight: 700 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

.glass-modal-close-btn {
    background: rgba(0, 0, 0, 0.05);
    border: none;
    border-radius: 50%;
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-muted);
    transition: var(--transition-smooth);
    cursor: pointer;
}

body.dark-theme .glass-modal-close-btn {
    background: rgba(255, 255, 255, 0.08);
}

.glass-modal-close-btn:hover {
    background: rgba(239, 68, 68, 0.1);
    color: #ef4444;
}

.glass-modal-body {
    padding: 2rem;
    overflow-y: auto;
}

.glass-modal-footer {
    padding: 1.25rem 2rem;
    border-top: 1.5px solid rgba(139, 115, 85, 0.1);
    display: flex;
    justify-content: flex-end;
    gap: 0.75rem;
}

@keyframes modalFadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Quick Actions Sidebar & Layout Custom Styles */
.quick-actions-sidebar {
    background: #ffffff;
    border-radius: var(--border-radius-lg, 16px);
    transition: var(--transition-smooth);
}

.btn-quick-action {
    border: 1.5px solid rgba(0, 0, 0, 0.05);
    background: #f8fafc;
    border-radius: 12px;
    padding: 1rem;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
}

.btn-quick-action:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.02);
    background: #ffffff;
}

.quick-action-icon {
    width: 44px;
    height: 44px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    transition: var(--transition-smooth);
}

.btn-quick-action:hover .quick-action-icon {
    transform: scale(1.1);
}

.btn-quick-action.action-register:hover {
    border-color: rgba(99, 102, 241, 0.3);
}

.btn-quick-action.action-manage:hover {
    border-color: rgba(16, 185, 129, 0.3);
}

body.dark-theme .quick-actions-sidebar {
    background: #1e1e2d;
    border-color: rgba(255, 255, 255, 0.05);
}

body.dark-theme .btn-quick-action {
    background: rgba(255, 255, 255, 0.02);
    border-color: rgba(255, 255, 255, 0.05);
}

body.dark-theme .btn-quick-action:hover {
    background: rgba(255, 255, 255, 0.04);
}
</style>
