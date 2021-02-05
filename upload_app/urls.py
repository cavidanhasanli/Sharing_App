from django.urls import path
from  upload_app.views import *
urlpatterns = [
    path('', home_views,name='home_page',),
    path('create-files/', create_files_views,name='create_file_page',),
    path('send_from/', send_from_views, name='send_from_page'),
    path('send_to/', send_to_views, name='send_to_page'),
    path('comment-room/<str:file_name>/',room,name='room_page')

]