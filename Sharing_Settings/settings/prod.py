from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
CELERY_BROKER_URL = os.environ["CELERY_BROKER_URL"]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ["DB_NAME"],
        'USER': os.environ["DB_USER"],
        'PASSWORD': os.environ["DB_PASSWORD"],
        'HOST': os.environ["DB_HOST"],
        'PORT': '5432',
    }
}
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(os.environ["CHANNELS_REDIS_HOST"], int(os.environ["CHANNELS_REDIS_PORT"]))],
        },
    },
}

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (os.path.join('static'),)