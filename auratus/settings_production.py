# flake8: noqa
import os.path

from .settings_shared import *

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), "templates"),)

MEDIA_ROOT = "/var/www/auratus/uploads/"
# put any static media here to override app served static media
STATICMEDIA_MOUNTS = ()

STATIC_ROOT = os.path.join(os.path.dirname(__file__), "../media")
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_OFFLINE = True

DEBUG = False
TEMPLATE_DEBUG = DEBUG

STATICFILES_DIRS = ()

AWS_S3_CUSTOM_DOMAIN = "d12khfts9rqjej.cloudfront.net"
AWS_IS_GZIPPED = True

AWS_STORAGE_BUCKET_NAME = "thraxil-auratus-static-prod"
AWS_PRELOAD_METADATA = True
DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"
STATICFILES_STORAGE = "cacheds3storage.MediaRootS3BotoStorage"
S3_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
STATIC_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_URL = STATIC_URL
DEFAULT_FILE_STORAGE = "cacheds3storage.MediaRootS3BotoStorage"
MEDIA_URL = S3_URL + "/media/"
COMPRESS_STORAGE = "cacheds3storage.CompressorS3BotoStorage"
AWS_QUERYSTRING_AUTH = False


if "migrate" not in sys.argv:
    INSTALLED_APPS = INSTALLED_APPS + [
        "raven.contrib.django.raven_compat",
    ]


try:
    from local_settings import *
except ImportError:
    pass
