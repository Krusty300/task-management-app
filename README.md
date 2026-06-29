# Task Management App

A full-stack task management application built with **React** and **Django**. This project demonstrates a complete CRUD application with user authentication, task management, and a clean modern UI.

---

## Features

### Authentication
- User registration with email
- JWT authentication
- Auto-login after registration
- Secure password storage

### Task Management
- Create, Read, Update, Delete tasks
- Mark tasks as Complete/Pending
- Filter tasks by status (All/Pending/Completed)
- Edit task titles and descriptions

### User Experience
- Real-time toast notifications
- Responsive design
- Clean UI with Mona Sans font
- Loading states

### Technical Features
- Django REST Framework API
- JWT token authentication
- User-specific task isolation
- CORS support
- Git version control

---

## Tech Stack

### Backend
| Technology | Version |
|------------|---------|
| Django | 5.2 |
| Django REST Framework | Latest |
| Django CORS Headers | Latest |
| Simple JWT | Latest |
| SQLite (Development) | - |

### Frontend
| Technology | Version |
|------------|---------|
| React | 18 |
| Axios | Latest |
| React Toastify | Latest |
| React Router DOM | Latest |
| Mona Sans Font | Variable |

---

## Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- pip
- npm

### Backend Setup

```bash
# Clone the repository
git clone https://github.com/Krusty300/task-management-app.git
cd task-management-app

# Create and activate virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install django djangorestframework django-cors-headers djangorestframework-simplejwt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Start the backend server
python manage.py runserver



# In a new terminal, navigate to frontend
cd frontend

# Install dependencies
npm install

# Start the React development server
npm start

Access the Application

Frontend: http://localhost:3000
Backend API: http://localhost:8000/api/
Admin Panel: http://localhost:8000/admin/


task-management-app/
├── backend/                    # Django project
│   ├── backend/                # Django settings
│   │   ├── settings.py         # Project settings
│   │   └── urls.py             # URL configuration
│   └── tasks/                  # Tasks app
│       ├── models.py           # Task model
│       ├── views.py            # API views
│       ├── serializers.py      # DRF serializers
│       └── admin.py            # Admin configuration
├── frontend/                   # React app
│   ├── src/
│   │   ├── components/         # React components
│   │   │   ├── Login.js
│   │   │   ├── Register.js
│   │   │   └── TaskList.js
│   │   ├── fonts/              # Font files
│   │   │   └── Mona-Sans.var.woff2
│   │   ├── api.js              # API service
│   │   ├── App.js              # Main App component
│   │   ├── fonts.css           # Font definitions
│   │   └── index.js            # Entry point
│   ├── public/
│   └── package.json
├── manage.py                   # Django management
├── .gitignore                  # Git ignore rules
└── README.md                   # This file


Database    Schema
Task        Model
Field	    Type	Description
id	        Integer	Primary key
user	    ForeignKey	User who owns the task
title	    CharField (200)	Task title
description	TextField	Task description (optional)
status	    CharField (20)	'pending' or 'completed'
created_at	DateTimeField	Creation timestamp
updated_at	DateTimeField	Last update timestamp