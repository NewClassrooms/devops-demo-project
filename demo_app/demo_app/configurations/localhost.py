from .common import Common


class Localhost(Common):
    DEBUG = True
    SECRET_KEY = 'not secret for development'

    ALLOWED_HOSTS = ['localhost']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': Common.BASE_DIR.parent / 'db.sqlite3',
        }
    }
