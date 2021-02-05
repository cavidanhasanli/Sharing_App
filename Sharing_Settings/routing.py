from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path  
from channels.auth import AuthMiddlewareStack  
import upload_app.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            upload_app.routing.websocket_urlpatterns 
            
        )
    ),
    
})