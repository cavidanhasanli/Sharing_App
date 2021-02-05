from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CELERY_BROKER_URL = 'redis://:p46cd8a6491d592e2092b7009bc3d0e45f21bcefa1b742a208887f2d4119b14b9@ec2-54-144-216-111.compute-1.amazonaws.com:27069'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (os.path.join('static'),)
