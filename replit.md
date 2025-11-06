# Flask Career Website - Job Hunter

## Overview
A simple career website built with Flask called "Job Hunter" that displays job listings and allows users to add new job postings. The application provides government and private job updates to help users find their dream job.

## Project Structure
```
.
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── templates/
│   ├── home.html          # Homepage template with job listings
│   └── add-job.html       # Form to add new job postings
├── static/
│   └── 294.jpg            # Hero image for homepage
└── replit.md              # This file
```

## Features
- Homepage displaying job listings and career resources
- Add job functionality with comprehensive form fields
- Job listings showing title, location, salary, description, and more
- Responsive design that works on desktop and mobile
- Career advice and job search tips sections

## Technical Details
- **Framework**: Flask 3.0.0
- **Python Version**: 3.11
- **Server**: Development - Flask dev server, Production - Gunicorn
- **Port**: 5000
- **Host**: 0.0.0.0 (allows all connections)

## Running the Application
The application is configured to run automatically via the workflow. It starts with:
```bash
python app.py
```

## Routes
- `GET /` - Homepage with job listings
- `GET /add-job` - Display form to add a new job
- `POST /add-job` - Submit new job posting

## Deployment
The application is configured for deployment using Gunicorn:
```bash
gunicorn --bind=0.0.0.0:5000 --reuse-port app:app
```

## Recent Changes
- **2025-11-06**: Fixed URL routing and template issues
  - Fixed app.py to properly handle /add-job route with GET and POST methods
  - Updated home.html to use Flask's url_for() for all links and static files
  - Fixed add-job.html to use Flask template syntax instead of Django syntax
  - Corrected template file naming (add-job.html) to match route calls
  - Updated form submission to capture all form fields properly
  - Verified application runs without errors

## Customization
To customize the website:
1. Edit `app.py` to modify the JOBS list or add new routes
2. Update `templates/home.html` to change the layout or content
3. Modify `static/css/style.css` to adjust styling and colors
4. Change the company name by updating the `company_name` variable in `app.py`
