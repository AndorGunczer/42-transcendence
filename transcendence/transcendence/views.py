from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def play(request):
    return render(request, 'play_menu.html', {})

def singleplayer(request):
    return render(request, 'singleplayer.html', {})

# def index(request):
#     return render(request, "/", {})