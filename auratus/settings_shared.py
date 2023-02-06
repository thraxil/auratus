# Django settings for auratus project.
import mimetypes
import os.path

import requests
from thraxilsettings.shared import common

base = os.path.dirname(__file__)
locals().update(common(app="auratus", base=base))

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(os.path.dirname(__file__), "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
                "django.template.context_processors.debug",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


INSTALLED_APPS += [  # noqa
    "bootstrapform",
    "auratus.main",
]

ALLOWED_HOSTS += [".thraxil.org", "auratus.fly.dev"]  # noqa

RETICULUM_UPLOAD = "https://reticulum.thraxil.org"
RETICULUM_PUBLIC = "https://d2f33fmhbh7cs9.cloudfront.net"


class ReticulumUploader(object):
    def upload(self, f):
        content_type = mimetypes.guess_type(f.name)[0]
        files = {"image": (f.name, f, content_type)}
        r = requests.post(RETICULUM_UPLOAD + "/", files=files, verify=True)
        return r.json()["hash"]


UPLOADER = ReticulumUploader()
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
