from django.urls import path
from transcendence import consumers

websocket_urlpatterns = [
    # path('/ws/chats/min(friend1_id, friend2_id)/max(friend1_id, friend2_id)', consumers.YourConsumer.as_asgi()),
    path('/ws/chats/{friend_id_min}/{friend_id_max}/', consumers.ChatConsumer.as_asgi()),
    path('/ws/friend_requests/{friend_id_min}/{friend_id_max}/', consumers.FriendRequestConsumer.as_asgi()),
]