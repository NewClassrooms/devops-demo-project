from configurations import values

from .common import Common


class Production(Common):
    DEBUG = False
    SECRET_KEY = values.SecretValue(environ_name='SECRET_KEY')

    ALLOWED_HOSTS = [
        '*',
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': values.Value('demo_app_prod', environ_name='POSTGRES_DBNAME'),
            'USER': values.SecretValue(environ_name='POSTGRES_USER'),
            'PASSWORD': values.SecretValue(environ_name='POSTGRES_PASSWORD'),
            'HOST': values.Value(None, environ_name='POSTGRES_HOST'),
            'PORT': values.PositiveIntegerValue(5432, environ_name='POSTGRES_PORT'),
        }
    }
