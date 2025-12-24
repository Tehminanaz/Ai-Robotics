# Authentication System Documentation

This document describes the authentication system implemented for the Robotics course platform.

## Overview

The authentication system provides secure user registration, login, and session management for the Robotics course platform. It includes custom fields for collecting user background information relevant to the course content.

## Features

### Core Authentication
- User registration with email and password
- Secure login with JWT token authentication
- Session management via localStorage
- Protected routes and API endpoints

### Custom User Fields
- **Software Background**: Allows users to specify their software development experience
- **Hardware Background**: Allows users to specify their hardware/robotics experience
- These fields are used to personalize the learning experience

### API Endpoints

#### Registration
- **Endpoint**: `POST /api/v1/auth/register`
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "securePassword123",
    "name": "John Doe",
    "software_background": "Python, JavaScript, React",
    "hardware_background": "Arduino, Raspberry Pi, Electronics"
  }
  ```
- **Response**:
  ```json
  {
    "access_token": "jwt_token_here",
    "token_type": "bearer",
    "user": {
      "id": "user_id",
      "email": "user@example.com",
      "name": "John Doe",
      "software_background": "Python, JavaScript, React",
      "hardware_background": "Arduino, Raspberry Pi, Electronics",
      "created_at": "2023-01-01T00:00:00"
    }
  }
  ```

#### Login
- **Endpoint**: `POST /api/v1/auth/login`
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "securePassword123"
  }
  ```
- **Response**: Same as registration

#### Get User Profile
- **Endpoint**: `GET /api/v1/auth/me`
- **Headers**: `Authorization: Bearer {token}`
- **Response**: User object without password

## Frontend Components

### AuthContext
- Manages user authentication state across the application
- Handles token storage and retrieval
- Provides `useAuth` hook for components

### LoginModal
- Modal component for login and registration
- Toggle between login and signup forms
- Collects custom background fields during registration
- Handles authentication errors

### AuthNavbar
- Navigation component that shows login/logout based on authentication status
- Displays user name when logged in
- Provides logout functionality

## Security

### Password Security
- Passwords are hashed using bcrypt with salt
- No plain text passwords are stored in the database

### Token Security
- JWT tokens are used for session management
- Tokens expire after 30 minutes of inactivity
- Tokens are stored in localStorage (for demo purposes)

### API Protection
- Protected endpoints require valid JWT tokens
- Invalid tokens result in 401 Unauthorized responses

## Database Schema

The authentication system uses a `users` table with the following structure:

```sql
CREATE TABLE users (
  id VARCHAR PRIMARY KEY,
  email VARCHAR UNIQUE NOT NULL,
  name VARCHAR NOT NULL,
  password_hash VARCHAR NOT NULL,
  software_background TEXT,
  hardware_background TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  is_active BOOLEAN DEFAULT TRUE
);
```

## Environment Variables

The following environment variables are required for authentication:

- `BETTER_AUTH_SECRET`: Secret key for JWT token signing (32+ character random string)
- `BETTER_AUTH_URL`: Base URL for the application (default: http://localhost:3000)

## Implementation Details

### Backend (FastAPI)
- Authentication logic is in `backend/auth.py`
- API routes are defined in `backend/api/auth.py`
- Database models are in the auth module
- Dependencies are managed in `backend/requirements.txt`

### Frontend (Docusaurus/React)
- Authentication context in `frontend/src/contexts/AuthContext.js`
- Login components in `frontend/src/components/Login/`
- Navigation components in `frontend/src/components/AuthNavbar/`

## Getting Started

1. Install backend dependencies: `pip install -r backend/requirements.txt`
2. Set environment variables in `.env`
3. Run database migrations: `python -m backend.migrations`
4. Start the backend: `uvicorn backend.main:app --reload`
5. Start the frontend: `npm start` in the frontend directory

## Testing

The authentication system can be tested using the following curl commands:

```bash
# Register a new user
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123",
    "name": "Test User",
    "software_background": "Python, JavaScript",
    "hardware_background": "Arduino, Electronics"
  }'

# Login
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123"
  }'
```

## Future Enhancements

- Social login providers (Google, GitHub)
- Email verification for new accounts
- Password reset functionality
- Refresh token implementation
- Two-factor authentication
- Role-based access control