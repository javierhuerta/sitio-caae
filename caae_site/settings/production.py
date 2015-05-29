# Send notification emails as a background task using Celery,
# to prevent this from blocking web server threads
# (requires the django-celery package):
# http://celery.readthedocs.org/en/latest/configuration.html

# import djcelery
#
# djcelery.setup_loader()
#
# CELERY_SEND_TASK_ERROR_EMAILS = True
# BROKER_URL = 'redis://'


# Use Redis as the cache backend for extra performance
# (requires the django-redis-cache package):
# http://wagtail.readthedocs.org/en/latest/howto/performance.html#cache

# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.cache.RedisCache',
#         'LOCATION': '127.0.0.1:6379',
#         'KEY_PREFIX': 'caae_site',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
#         }
#     }
# }

# Settings for production server
import os
DEBUG = False
TEMPLATE_DEBUG = DEBUG
ROOT_PATH = os.path.join(os.path.dirname(__file__), '..')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'caae',                      # Or path to database file if using sqlite3.
        'USER': 'caae',                      # Not used with sqlite3.
        'PASSWORD': '8S5cNU8jB6HTEQzj',                  # Not used with sqlite3.
        'HOST': 'mysql.unach.cl',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

COMPRESS_OFFLINE = True

ALLOWED_HOSTS = ['caae.unach.cl']


TEMPLATE_DIRS = (
    "/var/djangoprojects/sitio_caae_env/sitio_caae_env/templates",
    )

