from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def play(request):
    return render(request, 'play_menu.html', {})

def singleplayer(request):
    return render(request, 'singleplayer.html', {})

def game_single(request):
    return render(request, 'game_single.html', {})

def local(request):
    return render(request, 'local.html', {})

def game_local(request):
    return render(request, 'game_local.html', {})

# def index(request):
#     return render(request, "/", {})