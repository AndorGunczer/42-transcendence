from django.urls import path
# from .consumers import Chat

from . import views

urlpatterns = [
    path('', views.index, name='ind'),
	path('<str:receiver>/', views.dialog, name='d'),
	path('sendMsg', views.send, name='send_view'),
]

# websocket_urlpatterns = [
#     path('ws/chat/', Chat.as_asgi()),
# ]