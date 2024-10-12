
# Schedule Management API

This is a simple Django application that implements a CRUD API for managing a weekly schedule with IDs associated with time slots for each day of the week. The application also includes JWT authentication and Swagger documentation.

## Features
- CRUD operations for weekly schedules.
- JWT authentication for secure API access.
- Swagger documentation for easy API testing.
- Time slots for each day with customizable IDs.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd schedule_project
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional for accessing Django admin):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server:**
   ```bash
   python manage.py runserver 8000
   ```

   The application will run at `http://127.0.0.1:8000/`.

## JWT Authentication Setup

The API is protected by JWT (JSON Web Token) authentication. You need to obtain a token and pass it with your requests to access protected endpoints.

### Steps to Implement JWT Authentication:

1. **Install JWT authentication dependencies:**
   We are using `djangorestframework-simplejwt` for JWT authentication. Install the package:
   ```bash
   pip install djangorestframework-simplejwt
   ```

2. **Configure JWT in Django settings:**
   In your `settings.py`, configure Django REST Framework to use JWT for authentication:

   ```python
   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': (
           'rest_framework_simplejwt.authentication.JWTAuthentication',
       ),
   }

   SIMPLE_JWT = {
       'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
       'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
   }
   ```

3. **Add JWT token URLs to your `urls.py`:**
   In your main `urls.py`, include the following:

   ```python
   from rest_framework_simplejwt.views import (
       TokenObtainPairView,
       TokenRefreshView,
   )

   urlpatterns += [
       path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
       path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   ]
   ```

4. **Obtain JWT Token:**
   To authenticate, send a `POST` request to `/api/token/` with valid user credentials (username and password) to get a token:

   ```bash
   POST /api/token/
   {
     "username": "your_username",
     "password": "your_password"
   }
   ```

   Example using `curl`:
   ```bash
   curl -X POST http://127.0.0.1:8000/api/token/ -d "username=your_username&password=your_password"
   ```

   This will return an access token and a refresh token.

5. **Use the JWT Token in Requests:**
   After obtaining the token, include it in the `Authorization` header for all API requests:

   ```bash
   Authorization: Bearer <your_token>
   ```

   Example using `curl`:
   ```bash
   curl -H "Authorization: Bearer <your_token>" http://127.0.0.1:8000/api/timeslots/
   ```

6. **Refreshing the JWT Token:**
   When your access token expires, you can use the refresh token to get a new one by sending a `POST` request to `/api/token/refresh/`:

   ```bash
   POST /api/token/refresh/
   {
     "refresh": "your_refresh_token"
   }
   ```

   This will return a new access token.

## Running Tests(Unit Test)

To run the unit tests for the API, use the following command:

```bash
python manage.py test
```

## Swagger Documentation

The API has integrated Swagger documentation for easy testing and understanding of available endpoints. You can access the Swagger UI at:

```
http://127.0.0.1:8000/swagger/
```

