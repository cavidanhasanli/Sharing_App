from django.urls import re_path

from .consumers import *

websocket_urlpatterns = [
    re_path(r'file/(?P<file_name>\w+)/$', FileConsumer.as_asgi()),
]