# flake8: noqa
from settings_shared import *
import os.path

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
)

MEDIA_ROOT = '/var/www/auratus/uploads/'
# put any static media here to override app served static media
STATICMEDIA_MOUNTS = (
)

STATIC_ROOT = os.path.join(os.path.dirname(__file__), "../media")
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_OFFLINE = True

DEBUG = False
TEMPLATE_DEBUG = DEBUG

STATICFILES_DIRS = ()


if 'migrate' not in sys.argv:
    INSTALLED_APPS = INSTALLED_APPS + [
        'raven.contrib.django.raven_compat',
    ]


try:
    from local_settings import *
except ImportError:
    pass
