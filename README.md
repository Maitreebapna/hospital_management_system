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
```powershell
Copy-Item .env.example .env
# Edit .env and set SECRET_KEY, JWT_SECRET, SECURITY_PASSWORD_SALT,
# and INITIAL_ADMIN_PASSWORD before continuing.
.\.venv\Scripts\python.exe .\backend\init_db.py
```
The initial Admin email is `admin@hms.com`; its password is the value supplied as `INITIAL_ADMIN_PASSWORD`. The setup script does not create an Admin with a default password.

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

## Deploying on Render

This project is a Flask app. Render should use the repository root as the service root, install dependencies with `pip install -r requirements.txt`, and start the web service with `gunicorn --chdir backend app:app` (also configured in `Procfile`). There is no frontend build step: Flask serves the static Vue components from `frontend/`.

Set these environment variables in the Render service:

- `SECRET_KEY`, `JWT_SECRET`, and `SECURITY_PASSWORD_SALT`: independently generated, long random secrets.
- `DATABASE_URL`: a persistent Render PostgreSQL database URL, or leave unset to use SQLite. SQLite needs a Render persistent disk mounted where the database file is stored; without one, data is lost on redeploy/restart.
- `FRONTEND_URL`: optional frontend origin if the frontend is hosted separately. When set, CORS permits that origin for `/api/*`. If the frontend is served by this Flask app, leave it unset; API calls use same-origin URLs.
- `REDIS_URL`: optional Redis URL for the cache and Celery jobs. Without it, the app uses in-process caching; background and scheduled Celery jobs require Redis and separately running worker/Beat services.
- `MAIL_USERNAME`, `MAIL_PASSWORD`, and `MAIL_DEFAULT_SENDER`: optional SMTP credentials and sender address. `MAIL_SERVER`, `MAIL_PORT`, and `MAIL_USE_TLS` can override the SMTP defaults.
- `INITIAL_ADMIN_PASSWORD`: set this when running `backend/init_db.py` for the first time to create the initial admin user. Do not use a default or commit this value.

For PostgreSQL, the dependency list includes the PostgreSQL driver. Initialize the database once after configuring the service environment, using the Render shell or a one-off command:

```bash
python backend/init_db.py
```

## Project Structure
- `backend/`: Flask application, models, and background tasks.
- `frontend/`: Vue.js components and HTML entry points.
- `static_url_path`: Configured to serve `frontend/` from the root.
