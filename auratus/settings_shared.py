# Django settings for auratus project.
import os.path

from thraxilsettings.shared import common

base = os.path.dirname(__file__)
locals().update(common(app='auratus', base=base))

INSTALLED_APPS += [  # noqa
    'bootstrapform',
    'auratus.main',
]

ALLOWED_HOSTS += ['.thraxil.org']  # noqa

RETICULUM_BASE = "http://behemoth.ccnmtl.columbia.edu:14001/"
