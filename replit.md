# Flask Career Website

## Overview
A simple career website built with Flask that displays job listings. The application features a modern, responsive design with a purple gradient theme and showcases open positions at TechCorp.

## Project Structure
```
.
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── templates/
│   └── home.html          # Homepage template with job listings
├── static/
│   └── css/
│       └── style.css      # Styling for the website
└── replit.md              # This file
```

## Features
- Homepage displaying company branding and job listings
- Responsive design that works on desktop and mobile
- Job cards showing title, location, and salary information
- REST API endpoint at `/api/jobs` returning JSON data
- Modern gradient UI design

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

## API Endpoints
- `GET /` - Homepage with job listings
- `GET /api/jobs` - Returns job listings as JSON

## Deployment
The application is configured for deployment using Gunicorn:
```bash
gunicorn --bind=0.0.0.0:5000 --reuse-port app:app
```

## Recent Changes
- **2024-11-04**: Initial setup of Flask career website
  - Created Flask application with job listings
  - Implemented responsive HTML/CSS design
  - Configured workflow for port 5000
  - Set up deployment configuration with Gunicorn

## Customization
To customize the website:
1. Edit `app.py` to modify the JOBS list or add new routes
2. Update `templates/home.html` to change the layout or content
3. Modify `static/css/style.css` to adjust styling and colors
4. Change the company name by updating the `company_name` variable in `app.py`
