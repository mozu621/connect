"""
Django settings for api_connect project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from datetime import timedelta
import environ
import os

# このファイルからmanage.pyがある場所を示す。 __file__ → settings.py, dirname（） → connect/api_conect, dirname（dirname（）） → connect
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


env=environ.Env(DEBUG=(bool,False))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = env('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG=env('DEBUG')

ALLOWED_HOSTS=env.list('ALLOWED_HOSTS')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # 追加
    'django_filters', #追加 5/25
    'djoser',  # 追加
    'app.apps.ApiConfig',  # 追加
    'accounts.apps.AccountsConfig',  # 追加
    'corsheaders',  # 追加
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 追加
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    'http://next-js-connect-a3bk.vercel.app:3000'
]

CSRF_TRUSTED_ORIGINS    = ['next-js-connect-a3bk.vercel.app','127.0.0.1', 'connect-mozu.site']

CORS_ALLOW_HEADERS = [
  'accept',
  'accept-encoding',
  'authorization',
  'content-type',
  'origin',
  'dnt',
  'user-agent',
  'x-csrftoken',
  'x-requested-with']

ROOT_URLCONF = 'api_connect.urls'

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
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'api_connect.wsgi.application'

# 追加（DEFAULT_PERMISSION_CLASSES→認証の設定。IsAuthenticatedは認証されているユーザのみ許可
#　　　DEFAULT_AUTHENTICATION_CLASSES→認証はどのクラスを使うかの設定。JWTを使う）
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
}

# 追加Simple JWTの設定
SIMPLE_JWT = {
    # トークンをJWTに設定
    'AUTH_HEADER_TYPES': ('JWT',),
    # トークンの持続時間の設定
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60)
}

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'accounts.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
