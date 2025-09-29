# settings.py (relevant excerpts)
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'replace-with-secure-secret'
DEBUG = True   # set False in production

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'yourdomain.com']

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",  # your app
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

# Templates and static
TEMPLATES = [ ... ]  # default Django template config

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media (for avatar, prescriptions)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Email (for password reset / reminders) - replace with real SMTP config in prod
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# For production use SMTP settings:
# EMAIL_HOST = 'smtp.example.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = '...'
# EMAIL_HOST_PASSWORD = '...'
# EMAIL_USE_TLS = True

AUTH_USER_MODEL = 'core.User'  # custom user model (optional; shown below)
