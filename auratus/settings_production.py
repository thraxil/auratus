# flake8: noqa
from settings_shared import *

TEMPLATE_DIRS = (
    "/var/www/auratus/auratus/auratus/templates",
)

MEDIA_ROOT = '/var/www/auratus/uploads/'
# put any static media here to override app served static media
STATICMEDIA_MOUNTS = (
    ('/sitemedia', '/var/www/auratus/auratus/sitemedia'),
)

COMPRESS_ROOT = "/var/www/auratus/auratus/media/"
DEBUG = False
TEMPLATE_DEBUG = DEBUG

STATICFILES_DIRS = ()
STATIC_ROOT = "/var/www/auratus/auratus/media/"

if 'migrate' not in sys.argv:
    INSTALLED_APPS = INSTALLED_APPS + [
        'raven.contrib.django.raven_compat',
    ]


try:
    from local_settings import *
except ImportError:
    pass
