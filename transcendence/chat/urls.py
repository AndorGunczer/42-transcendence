from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='ind'),
	path('<str:receiver>', views.dialog, name='dialog'),
	path('sendMsg', views.send, name='send_view'),
]