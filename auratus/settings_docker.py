# flake8: noqa
import os.path

from thraxilsettings.docker import common

from .settings_shared import *

app = "auratus"
base = os.path.dirname(__file__)

locals().update(
    common(
        app=app,
        base=base,
        celery=False,
        INSTALLED_APPS=INSTALLED_APPS,
        STATIC_ROOT=STATIC_ROOT,
        MIDDLEWARE=MIDDLEWARE,
    )
)

ALLOWED_HOSTS = [".thraxil.org", "auratus.fly.dev"]  # noqa
