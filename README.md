# Library Management API Build With DjangoRestFramework

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


URL Configuration:

The project’s root urls.py includes routes for the API endpoints, admin panel, token authentication, and the browsable API login:

from django.contrib import admin

from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),       # App-level API routes
    path('api-auth/', include('rest_framework.urls')),  # Browsable API login
    path('api-token-auth/', obtain_auth_token), # Token auth endpoint
]


Usage


Access the Admin Panel:
Go to http://127.0.0.1:8000/admin/ to manage users and other models via Django's built-in admin.

Test API Endpoints via Browsable API:
Visit http://127.0.0.1:8000/api/users/ to interact with the user API. 

Use http://127.0.0.1:8000/api-auth/login/ for session-based authentication.

Obtain a Token:

Send a POST request to the token endpoint:

curl -X POST -d "username=admin&password=yourpassword" http://127.0.0.1:8000/api-token-auth/


API Endpoints

Users

GET /api/users/

List all users.

POST /api/users/

Create a new user.

GET /api/users/<user_id>/

Retrieve a specific user.

PUT/PATCH /api/users/<user_id>/

Update a specific user.

DELETE /api/users/<user_id>/
Delete a user.
