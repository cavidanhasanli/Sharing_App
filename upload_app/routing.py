from django.urls import re_path

from .consumers import *

websocket_urlpatterns = [
    re_path(r'ws/file/(?P<file_name>\w+)/$', FileConsumer.as_asgi()),
]