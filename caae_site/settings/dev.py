import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ROOT_PATH = os.path.join(os.path.dirname(__file__), '..')

# SQLite (simplest install)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT_PATH, 'db.sqlite3'),
    }
}

STATIC_ROOT = os.path.join(ROOT_PATH, 'static')
STATIC_URL = '/static/'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
