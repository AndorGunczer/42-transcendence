from django.urls import path
from transcendence import consumers

websocket_urlpatterns = [
    path('ws/communication/', consumers.CommunicationConsumer.as_asgi()),
]
