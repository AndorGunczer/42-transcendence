from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from transcendence.models import Users
from django.urls import reverse
from django.http import JsonResponse
# from rest_framework.decorators import api_view
from .menus import MENU_DATA

def index(request):
    return render(request, 'menu_general/index.html', {})

def indexPost(request, menu_type='main'):
    menu = MENU_DATA.get(menu_type)
    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

def play(request, menu_type='play_menu'):
    menu = MENU_DATA.get(menu_type)
    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

def singleplayer_menu(request, menu_type='singleplayer_menu'):
    menu = MENU_DATA.get(menu_type)
    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

def singleplayer_game(request, menu_type='singleplayer_game'):
    menu = MENU_DATA.get(menu_type)
    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

def local_menu(request, menu_type='local_menu'):
    menu = MENU_DATA.get(menu_type)
    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

def online_menu(request, menu_type='online_menu'):
    menu = MENU_DATA.get(menu_type)
    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

def local_game(request, menu_type='local_game'):
    menu = MENU_DATA.get(menu_type)
    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

def login(request, warning: str = None, menu_type='login'):
    menu = MENU_DATA.get(menu_type)
    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

def register(request, warning: str = None, menu_type='register'):
    menu = MENU_DATA.get(menu_type)
    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

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
            warning = e
            return HttpResponseRedirect(reverse("register", args=(warning,)))

    else:
        return HttpResponseRedirect(reverse("register"))

def login_check(request):
    pass

# def index(request):
#     return render(request, "/", {})