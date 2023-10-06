"""
WSGI config for demo_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_app.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Localhost')

# This needs to be imported after the configuration is defined
from configurations.wsgi import get_wsgi_application  # noqa: E402
application = get_wsgi_application()
