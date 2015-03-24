"""
Django settings for lwc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tr8el(=+#8!67*ug^59s-l+dmb6y!q)y&--wweq1tv*+^t-f%0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SOCIAL_AUTH_FACEBOOK_KEY = '1097331956950350'
SOCIAL_AUTH_FACEBOOK_SECRET = '15bbd2052d7284cb89f83bae9e8ff8c2'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', "user_groups"]

LOGIN_REDIRECT_URL = '/members'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'joins',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'lwc.middleware.ReferMiddleware',
)

ROOT_URLCONF = 'lwc.urls'

WSGI_APPLICATION = 'lwc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SHARE_URL = "http://launchwithcode.com/?ref="

TEMPLATE_DIRS = (
	os.path.join(BASE_DIR, 'templates'), # provides directory of templates regardless of os and provides portability
	#"C://Users//LIU\Google Drive//mystuff//lwc//templates",
	)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

#STATIC_ROOT = 'C:\Users\LIU\Google Drive\mystuff\lwc\static\static_root'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')

STATICFILES_DIRS = (
	 os.path.join(BASE_DIR, 'static', 'static_dirs'),
	#'C:\Users\LIU\Google Drive\mystuff\lwc\static\static_dirs',
) # collects static files to static root then is served to static url
# use python manage.py collectstatic

#MEDIA_ROOT = 'C:\Users\LIU\Google Drive\mystuff\lwc\static\media'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

MEDIA_URL = '/media/'