from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from transcendence.models import Users2
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
import copy

# from rest_framework.decorators import api_view
from .menus import MENU_DATA

# Neue Datei

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            data = response.data
            response = JsonResponse({"message": "Token created"}, status=200)
            response.set_cookie(
                'access_token', data['access'], httponly=True, secure=True, samesite='Strict'
            )
            print("Cookie Set in DJANGO")
            response.set_cookie(
                'refresh_token', data['refresh'], httponly=True, secure=True, samesite='Strict'
            )
        print("Refresh Cookie Set in DJANGO")
        return response

class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh_token')
        if not refresh_token:
            return JsonResponse({"error": "Refresh token missing"}, status=401)
        
        request.data['refresh'] = refresh_token
        response = super().post(request, *args, **kwargs)
        
        if response.status_code == 200:
            data = response.data
            response = JsonResponse({"message": "Token refreshed"}, status=200)
            response.set_cookie(
                'access_token', data['access'], httponly=True, secure=True, samesite='Strict'
            )
        return response

# HELPER FUNCTIONS

def validate_token(token):
    try:
        AccessToken(token)  # This will validate the token
        return True
    except (InvalidToken, TokenError):
        return False

def get_user_from_token(token):
    token = AccessToken(token)
    user_id = token.payload['user_id']
    user = Users2.objects.get(id=user_id)

    return user

def get_token_from_header(request):
    print(request)
    auth_header = request.headers.get('Authorization')
    print(auth_header)
    if auth_header and auth_header.startswith('Bearer '):
        print("return auth_header.split")
        return auth_header.split(' ')[1]  # Get the token part after 'Bearer'
    else:
        return None
    
def modify_json_menu(menu_type, token):
    menu = copy.deepcopy(MENU_DATA.get(menu_type))
    user = get_user_from_token(token)

    print(menu['headerItems'][0]['content'][1]['text'] )

    menu['headerItems'][0]['content'][1]['text'] = f'LOGGED IN AS {user}'
    menu['headerItems'][0]['content'][2]['text'] = f'wins: {user.wins}'
    menu['headerItems'][0]['content'][3]['text'] = f'losses: {user.losses}'

    if token and menu['menuTitle'] == 'Main Menu Buttons':
        del menu['menuItems'][4]['content'][0]
        menu['menuItems'][4]['content'][0]['class'] = 'menu-button'
    

    return menu
    
# VIEW FUNCTIONS

def index(request):
    return render(request, 'menu_general/index.html', {})

def indexPost(request, menu_type='main'):
    token = get_token_from_header(request)
    if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
        print(menu)
    else:
        menu = modify_json_menu(menu_type, token)
        print(menu)

    # # Validate the token
    # if not validate_token(token):
    #     return JsonResponse({'error': 'Unauthorized'}, status=401)
    
    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

def play(request, menu_type='play_menu'):
    token = get_token_from_header(request)
    if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
    else:
        menu = modify_json_menu(menu_type, token)
    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

def singleplayer_menu(request, menu_type='singleplayer_menu'):
    token = get_token_from_header(request)
    if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
    else:
        menu = modify_json_menu(menu_type, token)

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
    token = get_token_from_header(request)
    if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
    else:
        menu = modify_json_menu(menu_type, token)

    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

def online_menu(request, menu_type='online_menu'):
    token = get_token_from_header(request)
    if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
    else:
        menu = modify_json_menu(menu_type, token)

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
    token = get_token_from_header(request)
    if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
    else:
        menu = modify_json_menu(menu_type, token)

    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

def register(request, warning: str = None, menu_type='register'):
    token = get_token_from_header(request)
    if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
    else:
        menu = modify_json_menu(menu_type, token)

    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

@csrf_exempt
def registration_check(request):
    if request.method == "POST":
        try:
            print(request.POST)
            username = request.POST["username"]
            if username == '': raise Exception("username_not_specified")
            password = request.POST["password"]
            if password == '': raise Exception("password_not_specified")
            new_user = Users2(username=username, wins=0, losses=0)
            new_user.set_password(password)
            new_user.save()
            # Users.objects.create(username=username, password=Users.make_password(password), wins=0, losses=0, games=None)
            return JsonResponse(MENU_DATA.get('main'))
        except Exception as e:
            warning = e
            print(warning)
            return JsonResponse(MENU_DATA.get('register'))

    else:
        return JsonResponse(MENU_DATA.get('register'))

@csrf_exempt
def login_check(request):
    if request.method == "POST":
        try:
            check_if_user_exists = Users2.objects.filter(username=request.POST["username"]).exists()
            if check_if_user_exists:
                print("WHATSAPP")
                user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
                print(user)
                if user is not None:
                    # this user is valid, do what you want to do
                    pass
                else:
                    pass
                    # this user is not valid, he provided wrong password, show some error message
        except Exception as e:
            pass
    else:
        # there is no such entry with this username in the table
        pass

# def index(request):
#     return render(request, "/", {})