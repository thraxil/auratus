from settings_shared import *

TEMPLATE_DIRS = (
    "/var/www/auratus/auratus/templates",
)

MEDIA_ROOT = '/var/www/auratus/uploads/'
# put any static media here to override app served static media
STATICMEDIA_MOUNTS = (
    ('/sitemedia', '/var/www/auratus/auratus/sitemedia'),
)

COMPRESS_ROOT = "/var/www/auratus/auratus/media/"
DEBUG = False
TEMPLATE_DEBUG = DEBUG

try:
    from local_settings import *
except ImportError:
    pass
