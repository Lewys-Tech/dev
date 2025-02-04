# Library Management API

A robust, Django REST Framework-based API for managing a library system. This project provides endpoints for managing users, students, staff, other user types, and books, with token-based authentication and a browsable API interface for easy testing.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Management:**  
  Create, update, list, and delete users with fields such as first name, second name, email, phone, user role, status, and timestamps.
  
- **Token Authentication:**  
  Secure endpoints using Django REST Framework's token authentication mechanism.
  
- **Browsable API:**  
  Test your API interactively via the DRF browsable API.
  
- **Extensible Design:**  
  Easily extend the API with additional tables like Students, Staff, Other Users, and Books.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Lewys-Tech/dev.git


2.Create and Activate a Virtual Environment:

python -m venv web_app

source web_app/bin/activate      # On Unix or MacOS

web_app\Scripts\activate         # On Windows


3.Install Dependencies

pip install -r requirements.

4.Apply Migrations:

python manage.py migrate

5.Create a Superuser (for admin access):

python manage.py createsuperuser

6.Run the Development Server:

python manage.py runserver



Configuration

Django Settings:
The project uses Django REST Framework along with token authentication. Ensure that in your settings.py, you have:

INSTALLED_APPS = [
    # ...
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.admin',
    'django.contrib.auth',
    'user',  # Your app managing user models
    # other apps...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ]
}


