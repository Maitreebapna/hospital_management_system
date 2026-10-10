# Hospital Management System (HMS) 

A dynamic, full-stack Hospital Management platform designed to streamline medical administration. This system features three distinct Role-Based Access portals: an **Admin Dashboard** for creating doctors and analyzing hospital statistics, a **Doctor Dashboard** for managing appointments and charting patient treatments, and a **Patient Dashboard** for booking schedules and downloading CSV medical histories.

##  Technical Stack
- **Backend:** Python, Flask (RESTful API), SQLite (Primary DB), Redis (Caching & Job Broker)
- **Frontend:** Vue3, Bootstrap 5
- **Async Execution:** Celery (Worker & Beat)

## Project Setup (Windows PowerShell)

### 1. Requirements
Install Python and Redis, and make sure Redis is running on `127.0.0.1:6379`.

### 2. Installation
From the project root, create a virtual environment and install dependencies:
   ```bash
   py -m venv .venv
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

### 3. Database Initialization
Run this once from the project root to set up the SQLite database and default Admin account:
```bash
.\.venv\Scripts\python.exe .\backend\init_db.py
```
**Admin Credentials:**
- Email: `admin@hms.com`
- Password: `admin123`

## Running the Application
Open four PowerShell terminals in the project root. Start Redis first; the app uses it for caching and Celery jobs.

1. **Redis** (skip if the Redis service is already running):
   ```bash
   redis-server
   ```
   If `redis-server` is not on `PATH`, start Redis using the executable or service installed on your machine.
2. **Flask app**:
   ```powershell
   Set-Location .\backend
   ..\.venv\Scripts\python.exe .\app.py
   ```
3. **Celery Worker**:
   ```powershell
   Set-Location .\backend
   ..\.venv\Scripts\celery.exe -A app.celery_app worker --loglevel=info --pool=solo
   ```
4. **Celery Beat**:
   ```powershell
   Set-Location .\backend
   ..\.venv\Scripts\celery.exe -A app.celery_app beat --loglevel=info
   ```
   The worker and Beat are optional for the login and dashboards, but required for background and scheduled jobs.

Open `http://127.0.0.1:5000/` in your browser. Sign in with the Admin credentials below, or register a patient account.

## Project Structure
- `backend/`: Flask application, models, and background tasks.
- `frontend/`: Vue.js components and HTML entry points.
- `static_url_path`: Configured to serve `frontend/` from the root.
