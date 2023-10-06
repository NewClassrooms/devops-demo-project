import os

# Load the typical configurations. Doing this conditionally allows us to have
# different SecretValue items in different configurations without always
# having to specify all of them. For example, Production has SECRET_KEY as
# a SecretValue, but we don't need to specify that at all for Localhost.
configuration = os.environ.get('DJANGO_CONFIGURATION')
if configuration == 'Production':
    from .configurations.production import Production  # noqa: F401
elif configuration == 'Development':
    from .configurations.development import Development  # noqa: F401
elif configuration == 'Localhost':
    from .configurations.localhost import Localhost  # noqa: F401

# If a local configuration exists, load any classes it defines
if os.path.isfile(os.path.join(os.path.dirname(__file__), 'configurations', 'local.py')):
    from .configurations.local import *  # noqa: F401, F403
