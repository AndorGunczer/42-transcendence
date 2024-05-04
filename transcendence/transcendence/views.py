from django.shortcuts import render

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

def register(request):
    return render(request,  'menu_auth/register.html', {})

def registration_check(request):
    pass

def login_check(request):
    pass

# def index(request):
#     return render(request, "/", {})