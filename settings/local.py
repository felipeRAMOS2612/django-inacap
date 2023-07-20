from .base import *

DEBUG = config('DEBUG')

ALLOWED_HOSTS = ['*', 'http://localhost', 'http://127.0.0.1', 'http://localhost:3000']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=INNODB',
        },
        'NAME': config('DB_NAME_LOCAL'),
        'USER': config('DB_USER_LOCAL'),
        'PASSWORD': config('DB_PASSWORD_LOCAL'),
        'HOST':config('DB_HOST_LOCAL'),
        'PORT': config('DB_PORT_LOCAL', cast= int),
    }
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=50),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=90),
    "AUTH_HEADER_TYPES": ("Bearer")
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,"media")