# Django settings for auratus project.
import os.path

from thraxilsettings.shared import common

base = os.path.dirname(__file__)
locals().update(common(app='auratus', base=base))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(__file__), "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


INSTALLED_APPS += [  # noqa
    'bootstrapform',
    'auratus.main',
]

ALLOWED_HOSTS += ['.thraxil.org']  # noqa

RETICULUM_BASE = "http://reticulum.thraxil.org/"
