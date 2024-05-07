from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from transcendence.models import Users
from django.urls import reverse

def index(request):
    return render(request, 'menu_general/index.html', {})

def play(request):
    return render(request, 'menu_general/play_menu.html', {})

def singleplayer(request):
    return render(request, 'menu_general/singleplayer.html', {})

def game_single(request):
    return render(request, 'game_views/game_single.html', {})

def local(request):
    return render(request, 'menu_general/local.html', {})

def game_local(request):
    return render(request, 'game_views/game_local.html', {})

def login(request):
    return render(request, 'menu_auth/login.html', {})

def register(request, warning: str = None):
    return render(request,  'menu_auth/register.html', {warning: warning})

def registration_check(request):
    if request.method == "POST":
        try:
            username = request.POST["username"]
            if username == '': raise Exception("username_not_specified")
            password = request.POST["password"]
            if password == '': raise Exception("password_not_specified")
            Users.objects.create(username=username, password=password, score=0, games=None)
            return HttpResponseRedirect(reverse("index"))
        except Exception as e:
            return HttpResponseRedirect(reverse("register", args=(e,)))

    else:
        return HttpResponseRedirect(reverse("register"))

def login_check(request):
    pass

# def index(request):
#     return render(request, "/", {})