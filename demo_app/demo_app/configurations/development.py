from configurations import values

from .common import Common


class Development(Common):
    DEBUG = True
    SECRET_KEY = 'not secret for development'
    ALLOWED_HOSTS = [
        'demo_app-graphql',  # service name for CI test
        'localhost',  # allow port forwarding
    ]
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': values.Value('demo_app_dev', environ_name='POSTGRES_DBNAME'),
            'USER': values.SecretValue(environ_name='POSTGRES_USER'),
            'PASSWORD': values.SecretValue(environ_name='POSTGRES_PASSWORD'),
            'HOST': values.Value(None, environ_name='POSTGRES_HOST'),
            'PORT': values.PositiveIntegerValue(5432, environ_name='POSTGRES_PORT'),
        }
    }
