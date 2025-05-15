# CS551P_Assignment_3 – Hospital Directory Flask App 🏥

## Project Overview

This document outlines how to run and explore the solo Flask project **Hospital Directory App** — a healthcare listing and filtering platform built for the CS551P Advanced Programming assignment.

---

## No JavaScript

This project strictly adheres to the rule that **no `<script>` tags or JavaScript** were used in any template.  
All interactivity — from searching to filtering — is handled by the backend using Flask and Jinja2 only.

✅ Client-side behavior is rendered entirely via server-side logic — no frontend scripting required.

---

## Live Demo on Render

You can access the fully deployed web application here:  
🔗 **https://hospital-directory-flask.onrender.com**

---

## Running the App Locally via Codio

To run the app locally in your Codio workspace, follow these steps:

```bash
cd hospital_app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

Then open this URL in your browser:  
🔗 `https://your-codio-box-url:8000`

---

## Setting Up Before Making Changes

### Ensure Correct Python Version

Check your current Python version:

```bash
python3 --version
```

If it's not 3.10.7, create a `runtime.txt` file with this line:

```
python-3.10.7
```

This helps Render use the correct Python version for deployment.

---

## Cloning the GitHub Repository

To download and edit the code, clone the GitHub repository:

```bash
git clone https://github.com/varshitha0301/hospital-directory-flask.git
cd hospital-directory-flask
source venv/bin/activate
```

---

## HTML Templates Used

Here are the key templates used to render the pages:

- `index.html` – main page with hospital search and state filter  
- `hospital_detail.html` – individual hospital information view  
- `404.html` – error page shown for invalid or broken URLs  

Styling was applied with **Bootstrap 5** and Jinja2 templating — strictly **no JavaScript** involved.

---

## Source of Hospital Data

The dataset was sourced from:  
📍 [CMS Hospital General Information](https://data.cms.gov/provider-data/dataset/xubh-q36u)

Data was cleaned and reduced to retain:

- Hospital Name  
- Type  
- Ownership  
- Emergency Services  
- Ratings  
- Location details (City, State, ZIP)

⚠️ The dataset was trimmed to **5000 entries** for usability and performance.

---

## Dataset Cleanup & Rationale

### Cleanup Steps:
- Filtered out entries with incomplete data  
- Chose relevant columns for filtering and display  
- Merged location data for simplification  
- Assigned internal unique IDs

### Why:
- Met assignment requirements (2000–7000 entries)  
- Improved app speed and clarity  
- Simplified the user interface  
- Ensured fast loading and easy navigation

---

## Tech Stack & Feature Implementation

- Flask for server and routing  
- SQLAlchemy for ORM and database models  
- Bootstrap for layout and responsive styling  
- Flask forms and GET parameters for search/filter  
- Unit testing with `unittest`

---

## Key Components

- All routing defined in `app.py`  
- Database structure handled in `models.py`  
- Dataset preloaded from `Hospital_General_Information.csv`  
- Testing in `test_app.py`  
- Render deployment set up via `requirements.txt` and `gunicorn`

---

## Hosting Details

App deployed on Render with:

- Python version: 3.11.11  
- Build command: `pip install -r requirements.txt`  
- Start command: `gunicorn app:app`  
- Runtime config (optional): `runtime.txt`

---

## Final Notes

Hospital Directory is a well-structured Flask application that allows users to search and filter U.S. hospitals using verified open data.  
It fulfills all CS551P assignment guidelines with clean UI, filtering, testing, and zero JavaScript.

---

**GitHub username:** varshitha0301  
**Live App:** https://hospital-directory-flask.onrender.com
