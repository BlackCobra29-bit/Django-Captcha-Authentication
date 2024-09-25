# Django CAPTCHA Login

A simple Django application that implements a login page with CAPTCHA verification to enhance security against bot attacks.

## Features

- User login with email and password.
- CAPTCHA verification to prevent automated login attempts.
- Customizable templates using Bootstrap for responsive design.

## Requirements

- Python 3.x
- Django 3.x or higher
- `django-simple-captcha` library

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/BlackCobra29-bit/Django-Captcha-Authentication.git
cd Django-Captcha-Authentication-master
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install django django-simple-captcha
```

### 5. Add `captcha` to Installed Apps

Edit `settings.py` and add `'captcha'` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    # other apps
    'captcha',
]
```

### 6. Apply Migrations

Run the following command to create the necessary database tables:

```bash
python manage.py migrate
```