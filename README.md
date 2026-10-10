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
Copy `.env.example` to `.env`, replace the secret placeholders with strong, unique values, then initialize the database:

The initial Admin email is `admin@hms.com`; its password is the value supplied as `admin123`.

## Running the Application
Open PowerShell terminals in the project root. To run Celery jobs locally, start Redis and set `REDIS_URL=redis://localhost:6379/0` in `.env`. Without Redis, the app uses in-process caching and background jobs are unavailable.

1. **Redis** (only needed for Celery jobs; skip if the Redis service is already running):
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

Open `http://127.0.0.1:5000/` in your browser. Sign in with the configured Admin account, or register a patient account.


## Project Structure
- `backend/`: Flask application, models, and background tasks.
- `frontend/`: Vue.js components and HTML entry points.
- `static_url_path`: Configured to serve `frontend/` from the root.
