"""
URL configuration for transcendence project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import CustomTokenObtainPairView, CustomTokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('indexPost', views.indexPost, name="indexPost"),
    path('play', views.play, name="play"),
    path('singleplayer_menu', views.singleplayer_menu, name="singleplayer_menu"),
    path('singleplayer_game', views.singleplayer_game, name="singleplayer_game"),
    path('local_menu', views.local_menu, name="local_menu"),
    path('local_game', views.local_game, name="local_game"),
    path('online_menu', views.online_menu, name="online_menu"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('register/<str:warning>/', views.register, name="register"),
    path('login_check', views.login_check, name="login_check"),
    path('registration_check', views.registration_check, name="registration_check"),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('logout', views.logout, name='logout'),
]
