"""Project settings."""

import sys

from dynaconf import LazySettings


# --- BEGIN OF DYNACONF HEADER ---
settings = LazySettings(
    GLOBAL_ENV_FOR_DYNACONF='GALAXY',

)
# --- END OF DYNACONF HEADER ---

# ---------------------------------------------------------
# Django settings
# ---------------------------------------------------------

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',

    'rest_framework',

    'galaxy_api.api',
    'galaxy_api.auth',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'galaxy_api.urls'

AUTH_USER_MODEL = 'galaxy_auth.user'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
            ],
        },
    },
]


WSGI_APPLICATION = 'galaxy_api.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': settings.get('DB_NAME', 'galaxy'),
        'USER': settings.get('DB_USER', 'galaxy'),
        'PASSWORD': settings.get('DB_PASSWORD', ''),
        'HOST': settings.get('DB_HOST', 'localhost'),
        'PORT': settings.get('DB_PORT', ''),
    }
}


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

# ---------------------------------------------------------
# Third party libraries settings
# ---------------------------------------------------------

# Rest Framework

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'galaxy_api.auth.auth.RHIdentityAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'galaxy_api.auth.auth.RHEntitlementRequired',
    ]
}

RH_ENTITLEMENT_REQUIRED = 'insights'

# ---------------------------------------------------------
# Application settings
# ---------------------------------------------------------

API_PATH_PREFIX = 'api'

# --- BEGIN OF DYNACONF FOOTER ---
settings.populate_obj(sys.modules[__name__])
# --- END OF DYNACONF FOOTER ---
