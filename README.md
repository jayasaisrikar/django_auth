# Django Authentication Project

This project is a Django-based web application that implements a comprehensive authentication system. It includes features such as user registration, login (with email or username), logout, password change, and password reset functionality.

## Features

- User registration with email and username
- Login with either email or username
- Logout functionality
- Password change for authenticated users
- Password reset via email
- User dashboard and profile views
- Bootstrap 4 for frontend styling

## Project Structure

```
django_auth_project/
│
├── django_auth_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   │   └── accounts/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── signup.html
│   │       ├── password_change.html
│   │       ├── dashboard.html
│   │       └── profile.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── backends.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
└── requirements.txt
```

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/django-auth-project.git
   cd django-auth-project
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply the database migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Open a web browser and navigate to `http://127.0.0.1:8000` to see the application.

## Usage

- Visit the home page and use the navigation links to access different features.
- Register a new account using the Sign Up page.
- Log in using either your email or username.
- Once logged in, you can view your dashboard, change your password, or update your profile.
- Use the "Forgot Password" link on the login page to reset your password via email.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.