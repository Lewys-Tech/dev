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
   git clone https://github.com/<your_username>/<your_repository>.git
   cd <your_repository>
