import os
"""
Django settings for openuniverse project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nw1o9-jssq-u6q&wi7rt6z=ar@%l%zrv$-#%6n0!iwh99_7iz_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

'''Allowed Hosts:
    A list of strings representing the host/domain names that this Django site can serve.
    This is a security measure to prevent HTTP Host header attacks, which are possible even under many seemingly-safe web server configurations.
'''
ALLOWED_HOSTS = ['openuniverse.me','206.189.177.194', '127.0.0.1']


'''
    Installed Apps:
    A list of strings designating all applications that are enabled in this Django installation.
    Each string should be a dotted Python path to:
'''
INSTALLED_APPS = [
    'website.apps.WebsiteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mathfilters',
    'rest_framework',
    'api'
]

'''
    Midleware:
    A framework of hooks into Django’s request/response processing.
    It’s a light, low-level “plugin” system for globally altering Django’s input or output.
'''
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
 
ROOT_URLCONF = 'openuniverse.urls'

'''
    Templates:
    A list containing the settings for all template engines to be used with Django.
    Each item of the list is a dictionary containing the options for an individual engine.
'''
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['website/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
            'libraries': {
                'to_datetime':'openuniverse.templatetags.to_datetime',
                'duration':'openuniverse.templatetags.duration'},
        },
    },
]

WSGI_APPLICATION = 'openuniverse.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

'''
    Databases:
    A dictionary containing the settings for all databases to be used with Django.
    It is a nested dictionary whose contents map a database alias to a dictionary containing the options for an individual database.
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'openuniversedb',
        'USER': os.environ['DJANGO_DB_USER'],
        'PASSWORD': os.environ['DJANGO_DB_PASS'],
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
# URL to use when referring to static files located in STATIC_ROOT:
STATIC_URL = '/static/'

'''
    This setting defines the additional locations the staticfiles app will traverse if the FileSystemFinder finder is enabled, e.g.
    If you use the collectstatic or findstatic management command or use the static file serving view.
'''
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "website/static"),
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '200/day',
        'user': '2000/day'
    },
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}
