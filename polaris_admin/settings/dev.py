# """
# Django settings for polaris_admin project.
#
# Generated by 'django-admin startproject' using Django 3.1.7.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/3.1/topics/settings/
#
# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/3.1/ref/settings/
# """
#
# from pathlib import Path
# import  sys
# import os
# import datetime
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
# # add apps dir
# sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
#
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'a0y66j4my@vnf&fqhji$pv5nur(bu4ku#8+_w(v6-l+x*z-#yg'
#
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# ALLOWED_HOSTS = ["*"]
#
#
# # Application definition
#
# INSTALLED_APPS = [
#     # 'simpleui',
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework',
#     'oauth',
#     'system'
# ]
#
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
#
# ROOT_URLCONF = 'polaris_admin.urls'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = 'polaris_admin.wsgi.application'
#
#
# # Database
# # https://docs.djangoproject.com/en/3.1/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
#
#
# # Password validation
# # https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
#
#
# # Internationalization
# # https://docs.djangoproject.com/en/3.1/topics/i18n/
#
# LANGUAGE_CODE = 'zh-hans'
#
# TIME_ZONE = 'Asia/Shanghai'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True
#
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.1/howto/static-files/
#
# STATIC_URL = '/static/'
#
#
# # 指定自定义的用户模型
# AUTH_USER_MODEL = 'oauth.Users'
#
# # DRF配置
# REST_FRAMEWORK = {
#
#     'DEFAULT_PERMISSION_CLASSES':
#         (
#             'rest_framework.permissions.IsAuthenticated',  # 登录验证
#             'polaris_admin.utils.permissions.RbacPermission',  # 自定义权限认证
#         ),
#     'DEFAULT_AUTHENTICATION_CLASSES':
#         (
#             'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # DRF-JWT认证
#         ),
# }
#
#
# JWT_AUTH = {
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),  # Token有效时间
#     'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),  # Token刷新有效时间
#     'JWT_ALLOW_REFRESH': True,  # 允许刷新Token
#     'JWT_AUTH_HEADER_PREFIX': 'Bearer',  # 定义Token携带头信息, Authorization: Bearer ...
# }
#
# AUTHENTICATION_BACKENDS = [
#     'oauth.utils.UsernameMobileAuthBackend',  # 自定义用户认证方法
# ]
#
#
# BASE_API = 'api/'  # 项目BASE API, 如设置时必须以/结尾
# WHITE_LIST = [f'/{BASE_API}oauth/login/', f'/{BASE_API}oauth/info/', f'/{BASE_API}swagger/.*']  # 权限认证白名单
# REGEX_URL = '^{url}$'  # 权限匹配时,严格正则url
#
#
# # Redis
# REDIS_PWD = os.getenv('REDIS_PWD', '')
# REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
# REDIS_PORT = os.getenv('REDIS_PORT', '6379')
# if REDIS_PWD:
#     REDIS_STR = f':{REDIS_PWD}@'
# else:
#     REDIS_STR = ''
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': f'redis://{REDIS_STR}{REDIS_HOST}:{REDIS_PORT}/0',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         }
#     },
#     # 用户信息/ip黑名单
#     'user_info': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': f'redis://{REDIS_STR}{REDIS_HOST}:{REDIS_PORT}/2',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         }
#     },
#
# }

"""
Django settings for polaris_admin project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import  sys
import os
import datetime
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# add apps dir
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a0y66j4my@vnf&fqhji$pv5nur(bu4ku#8+_w(v6-l+x*z-#yg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'oauth',
    'system'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #DRF response middleware
    'polaris_admin.utils.middleware.ResponseMiddleware',
]

ROOT_URLCONF = 'polaris_admin.urls'

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

WSGI_APPLICATION = 'polaris_admin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'swagger',
        'NAME': 'learning_drf',
        'USER': 'root',
        'PASSWORD': 'Mysqlrootpassword',
        'HOST': '10.72.244.88',
        'PORT': '3306',
      # 'ENGINE': ' ',
      # 'NAME': BASE_DIR / 'db.sqlite3',

    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_PWD = os.getenv('DEFAULT_PWD', '123456')  # 创建用户默认密码

# 指定自定义的用户模型
AUTH_USER_MODEL = 'oauth.Users'

# DRF配置
REST_FRAMEWORK = {
    # 全局异常处理
    'EXCEPTION_HANDLER': 'polaris_admin.utils.exceptions.exception_handler',
    #全局分页设置
    'DEFAULT_PAGINATION_CLASS': 'polaris_admin.utils.pagination.GlobalPagination',
    'DEFAULT_PERMISSION_CLASSES':
        (
            'rest_framework.permissions.IsAuthenticated',  # 登录验证
            'polaris_admin.utils.permissions.RbacPermission',  # 自定义权限认证
        ),
    'DEFAULT_AUTHENTICATION_CLASSES':
        (
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # DRF-JWT认证
        ),
}


JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=10),  # Token有效时间
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),  # Token刷新有效时间
    'JWT_ALLOW_REFRESH': True,  # 允许刷新Token
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',  # 定义Token携带头信息, Authorization: Bearer ...
}

AUTHENTICATION_BACKENDS = [
    'oauth.utils.UsernameMobileAuthBackend',  # 自定义用户认证方法
]


BASE_API = 'api/'  # 项目BASE API, 如设置时必须以/结尾
WHITE_LIST = [f'/{BASE_API}oauth/login/', f'/{BASE_API}oauth/info/', f'/{BASE_API}swagger/.*']  # 权限认证白名单
REGEX_URL = '^{url}$'  # 权限匹配时,严格正则url


# Redis
REDIS_PWD = os.getenv('REDIS_PWD', '')
REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.getenv('REDIS_PORT', '6379')
if REDIS_PWD:
    REDIS_STR = f':{REDIS_PWD}@'
else:
    REDIS_STR = ''
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_STR}{REDIS_HOST}:{REDIS_PORT}/0',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    # 用户信息/ip黑名单
    'user_info': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_STR}{REDIS_HOST}:{REDIS_PORT}/2',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },

}