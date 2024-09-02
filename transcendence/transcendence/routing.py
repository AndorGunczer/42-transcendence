from django.urls import path
from transcendence import consumers

websocket_urlpatterns = [
    path('wss/communication/', consumers.CommunicationConsumer.as_asgi()),
]
