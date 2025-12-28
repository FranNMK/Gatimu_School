# Gatimu School Website

## Overview
This is the official website for Gatimu School, a premier learning institution. The website is built using **Django** (Python) and **Bootstrap 5**, providing a modern, responsive, and dynamic platform for school information, galleries, and contact management.

## Features
- **Dynamic Content:**
  - **Vision & Mission:** Manageable via the Admin Panel.
  - **Gallery:** Upload images dynamically via Admin.
- **Home Page:** Hero section, Key highlights, and dynamic Vision/Mission display.
- **About Page:** Detailed school overview (static) and dynamic Vision/Mission.
- **Gallery Page:** Grid layout with "Read More" modals and dynamic truncated descriptions.
- **Contact Page:** Functional contact form (saves to database) with success messages.
- **Portal:** Placeholder for future student/parent login.
- **Admin Panel:** Full control over Contact Messages, Gallery Images, and School Info.

## Technologies Used
- **Backend:** Django 5.2.8 (Python)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite (default for dev) / PostgreSQL (recommended for production)
- **Static Files:** Whitenoise (for production serving)
- **Deployment:** Ready for Render / Heroku

## Installation & Setup

### Prerequisites
- Python 3.8+ installed
- Git installed

### Steps
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd gatimu_school
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   # Activate it:
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server**
   ```bash
   python manage.py runserver
   ```
   Access the site at `http://127.0.0.1:8000/`.

## Admin Access
- URL: `http://127.0.0.1:8000/admin/`
- **Default Credentials** (if set up during dev):
  - Username: `frank`
  - Password: `123`

## Deployment (Render)
1. Push code to GitHub.
2. Create a new **Web Service** on Render.
3. Connect repository.
4. **Build Command:** `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
5. **Start Command:** `gunicorn gatimu_school.wsgi`
6. Add Environment Variable: `PYTHON_VERSION` (e.g., 3.9.0)

## Brand Colors
- **Primary (Dark Blue):** `#002147` (Navbar, Headings)
- **Secondary (Green):** `#10B981` (Highlights, Buttons)
- **Accent (Light Blue):** `#3B82F6` (Action Buttons)

---
© 2025 Gatimu School. All Rights Reserved.
