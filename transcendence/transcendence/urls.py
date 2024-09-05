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
from .views import  CustomTokenRefreshView

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),
    # MAIN MENUS
    path('', views.index, name="index"),
    path('indexPost', views.indexPost, name="indexPost"),
    path('play', views.play, name="play"),
    path('match_history', views.match_history, name="match_history"),
    # GAMES
    path('singleplayer_menu', views.singleplayer_menu, name="singleplayer_menu"),
    path('singleplayer_game', views.singleplayer_game, name="singleplayer_game"),
    path('local_menu', views.local_menu, name="local_menu"),
    path('local_check', views.local_check, name="local_check"),
    path('local_game', views.local_game, name="local_game"),
    path('close_local', views.close_local, name="close_local"),
    path('online_menu', views.online_menu, name="online_menu"),
    # TOURNAMENT URLS
    path('tournament_main', views.tournament_main, name="tournament_main"),
    path('tournament_create', views.tournament_create, name="tournament_create"),
    path('tournament_create_check', views.tournament_create_check, name="tournament_create_check"),
    path('tournament_select', views.tournament_select, name="tournament_select"),
    path('tournament_game_check', views.tournament_game_check, name="tournament_game_check"),
    path('close_tournament_game', views.close_tournament_game, name="close_tournament_game"),
    # AUTHENTICATION URLS
    path('login', views.login, name="login"),
    path('verify_otp', views.verify_otp_view, name='verify_otp'),
    path('register', views.register, name="register"),
    path('register/<str:warning>/', views.register, name="register"),
    path('upload_file', views.upload_file, name="upload_file"),
    path('login_check', views.login_check, name="login_check"),
    path('registration_check', views.registration_check, name="registration_check"),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('api/csrf-token/', views.get_csrf_token, name='csrf-token'),
    path('logout', views.logout, name='logout'),
    path('settings', views.load_settings, name='settings'),
    path('delete_user_stats', views.delete_user_stats, name='delete_user_stats'),
    path('save_changes', views.save_changes, name='save_changes'),
    # FRIENDS
    path('profile', views.profile, name="profile"),
]
