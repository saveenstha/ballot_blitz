from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# ── Security ───────────────────────────────────
# Read SECRET_KEY from environment variable (set this in Render dashboard)
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-local-dev-key-change-me')

# DEBUG = False in production (Render sets RENDER env var automatically)
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ["*"]

# In production, allow the Render domain and any custom domain
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'game',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.common.CommonMiddleware',

]

ROOT_URLCONF = 'ballot_blitz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'ballot_blitz.wsgi.application'
# ── Static files (WhiteNoise) ───────────────────
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'           # collectstatic dumps here
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
