from django.urls import path
from login_register_app.views import *

urlpatterns = [
    path("register/", register, name='register'),
    path('', login, name='login'),
    path('logout/', logout, name='logout'),
]