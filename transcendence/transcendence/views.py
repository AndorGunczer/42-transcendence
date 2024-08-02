# Functions as to what the server should do upon requests at specific urls

from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from transcendence.models import Users2, Tournaments, Participants, Players, Games, Avatar
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
from django.middleware.csrf import get_token
import json
import random
from transcendence.web3_utils import add_tournament_to_blockchain, query_blockchain
from .menus import MENU_DATA

# Initial Load of Site

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

# Utilize Access Tokens

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

# Modify JSON Menus with Dynamic data
    
def modify_json_menu(menu_type, token):
    menu = copy.deepcopy(MENU_DATA.get(menu_type))
    user = get_user_from_token(token)

    print(menu['headerItems'][0]['content'][1]['text'] )

    menu['headerItems'][0]['content'][1]['text'] = f'LOGGED IN AS {user}'
    menu['headerItems'][0]['content'][2]['text'] = f'wins: {user.wins}'
    menu['headerItems'][0]['content'][3]['text'] = f'losses: {user.losses}'

    menu['headerItems'].append({
        'id': 2,
        'type': 'button',
        'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
        'text': 'SETTINGS',
        'onclick': 'settings()',
    })

    menu['headerItems'].append({
                'id': 3,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': 'LOGOUT',
                'onclick': 'logout()'
    })

    menu['headerItems'][0]['content'].append({
                'type': 'img',
                'src': f'{user.avatarDirect}',
                'identifier': 'avatarPic'
    })

    if token and menu['menuTitle'] == 'Main Menu Buttons':
        del menu['menuItems'][4]
        # menu['menuItems'][0]['content'][0]['class'] = 'menu-button'
    

    return menu

def tournament_select_fill(menu):
    tournament_list = Tournaments.objects.all()

    for tournament in tournament_list:
        menu['menuItems'][0]['content'][0]['content'].append({
            'type': 'option',
            'value': tournament.name,
            'text': tournament.name
        })

    print("tournament_select_fill(menu) called")
    
    return menu

from django.db.models import Q

from django.db.models import Q

def tournament_select_page_fill(menu, participants):
    # for participant in participants:
    #     menu['menuItems'][0]['content'][0]['content'].append({
    #         'type': 'div',
    #         'class': 'participant',
    #         'content': [
    #             {
    #                 'type': 'p',
    #                 'text': participant.player.username,
    #             },
    #             {
    #                 'type': 'p',
    #                 'text': f'{participant.points}'
    #             }
    #         ]
    #     })

    menu['menuItems'][0]['content'][0]['content'].append({
        'type': 'table',
        'content': [
            {
                'type': 'thead',
                'class': 'thead-dark text-white',
                'content': [
                    {
                        'type': 'td',
                        'class': 'text-white',
                        'text': '#'
                    },
                    {
                        'type': 'td',
                        'class': 'text-white',
                        'text': 'Player'
                    },
                    {
                        'type': 'td',
                        'class': 'text-white',
                        'text': f'Points'
                    }                    
                ]
            }
        ]
    })

    table = menu['menuItems'][0]['content'][0]['content']

    for i,participant in enumerate(participants):
        table.append({
            'type': 'tr',
            'class': 'participant text-white',
            'content': [
                {
                    'type': 'td',
                    'class': 'text-white',
                    'text': f'{i}'
                },
                {
                    'type': 'td',
                    'class': 'text-white',
                    'text': participant.player.username,
                },
                {
                    'type': 'td',
                    'class': 'text-white',
                    'text': f'{participant.points}'
                }
            ]
        })

#     <table class="table">
#   <thead class="thead-dark">
#     <tr>
#       <th scope="col">#</th>
#       <th scope="col">First</th>
#       <th scope="col">Last</th>
#       <th scope="col">Handle</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th scope="row">1</th>
#       <td>Mark</td>
#       <td>Otto</td>
#       <td>@mdo</td>
#     </tr>
#     <tr>
#       <th scope="row">2</th>
#       <td>Jacob</td>
#       <td>Thornton</td>
#       <td>@fat</td>
#     </tr>
#     <tr>
#       <th scope="row">3</th>
#       <td>Larry</td>
#       <td>the Bird</td>
#       <td>@twitter</td>
#     </tr>
#   </tbody>
# </table>

    if participants:
        # Assuming all participants are from the same tournament
        tournament_id = participants[0].tournament_id

        # Correctly formed query to get the first Game where result is either None or 'Not Set' and matches the given tournament_id
        first_game_with_empty_result = Games.objects.filter(
            (Q(result__isnull=True) | Q(result='Not Set')) & Q(tournament_id=tournament_id)
        ).order_by('id').first()


        if first_game_with_empty_result:
            players_of_game = Players.objects.filter(game=first_game_with_empty_result.id)
            if len(players_of_game) >= 2:
                menu['menuItems'][0]['content'][1]['text'] = f'{players_of_game[0].player.username} vs {players_of_game[1].player.username}'
            else:
                top_participant = Participants.objects.filter(tournament=tournament_id).order_by('-points').first()
                if top_participant:
                    menu['menuItems'][0]['content'][1]['text'] = f'Winner: {top_participant.player.username}'
                else:
                    menu['menuItems'][0]['content'][1]['text'] = 'Winner: Unknown'
        else:
            top_participant = Participants.objects.filter(tournament=tournament_id).order_by('-points').first()
            if top_participant:
                menu['menuItems'][0]['content'][1]['text'] = f'Winner: {top_participant.player.username}'
            else:
                menu['menuItems'][0]['content'][1]['text'] = 'Winner: Unknown'
            del menu['menuItems'][0]['content'][2]
    else:
        menu['menuItems'][0]['content'][1]['text'] = 'No participants found'

    print('tournament_select_page_fill() called')
    return {'menu': menu, 'game': first_game_with_empty_result.id if first_game_with_empty_result else None}

    
# VIEW FUNCTIONS

# Initial Website Load

def index(request):
    token = get_token_from_header(request)
    if (token == None) or (not validate_token(token)):
        obj = {
            'username': 'Guest',
            'wins': 'None',
            'losses': 'None',
        }
        return render(request, 'menu_general/index.html', obj)
    else:
        user = get_user_from_token(token)
        obj = {
            'username': user.username,
            'wins': user.wins,
            'losses': user.losses,
        }
        print(obj)
        return render(request, 'menu_general/index.html', obj)

# Site loads with JSON Data

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

# GAMES
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

def local_check(request, menu_type='local_game'):
    token = get_token_from_header(request)

    data = json.loads(request.body)
    player1 = data.get("player1")
    player2 = data.get("player2")

    if not Users2.objects.get(username=player1):
        JsonResponse({'error': str(e)}, status=403)
    elif not Users2.objects.get(username=player2):
        JsonResponse({'error': str(e)}, status=403)
    else:
        # create game database instance and 2 player instances joined into game
        game_db = Games()
        game_db.save()
        player1_db = Players(player=Users2.objects.get(username=player1), game=game_db)
        player1_db.save()
        player2_db = Players(player=Users2.objects.get(username=player2), game=game_db)
        player2_db.save()

        # if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
        # else:
        #     menu = modify_json_menu(menu_type, token)

        if menu is not None:
            response_data = {'player1': player1, 'player2': player2, 'player1_id': player1_db.id, 'player2_id': player2_db.id}
            return JsonResponse(response_data, status=200)
        else:
            return JsonResponse({'error': 'Menu type not found'}, status=404)

from django.core.exceptions import ObjectDoesNotExist

# Database Manipulation based on the results of Local Game

def close_local(request, menu_type='main'):
    try:
        token = get_token_from_header(request)

        data = json.loads(request.body)
        player1 = data.get('player1')
        player2 = data.get('player2')

        if player1.get('status') == 'winner':
            player1_db = Users2.objects.get(username=player1.get('name'))
            player1_db.wins += 1
            player1_db.save()

            player2_db = Users2.objects.get(username=player2.get('name'))
            player2_db.losses += 1
            player2_db.save()

            player_id = player1.get('id')
            if player_id is None:
                return JsonResponse({'error': 'Player 1 ID not provided'}, status=400)

            try:
                player = Players.objects.get(id=player_id)
                game = Games.objects.get(id=player.game.id)
                game.result = player1.get('name')
                game.save()
            except Players.DoesNotExist:
                return JsonResponse({'error': 'Player 1 not found'}, status=404)
            except Games.DoesNotExist:
                return JsonResponse({'error': 'Game not found'}, status=404)

        else:
            player1_db = Users2.objects.get(username=player1.get('name'))
            player1_db.losses += 1
            player1_db.save()

            player2_db = Users2.objects.get(username=player2.get('name'))
            player2_db.wins += 1
            player2_db.save()

            player_id = player1.get('id')
            if player_id is None:
                return JsonResponse({'error': 'Player 1 ID not provided'}, status=400)

            try:
                player = Players.objects.get(id=player_id)
                game = Games.objects.get(id=player.game.id)
                game.result = player2.get('name')
                game.save()
            except Players.DoesNotExist:
                return JsonResponse({'error': 'Player 1 not found'}, status=404)
            except Games.DoesNotExist:
                return JsonResponse({'error': 'Game not found'}, status=404)

        # Determine the menu based on the token
        if (token is None) or (not validate_token(token)):
            menu = copy.deepcopy(MENU_DATA.get(menu_type))
        else:
            menu = modify_json_menu(menu_type, token)

        # Return the menu if found, else return an error response
        if menu is not None:
            return JsonResponse(menu)
        else:
            return JsonResponse({'error': 'Menu type not found'}, status=404)

    except Users2.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


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

# TOURNAMENT

# Loading the first menu of tournament

def tournament_main(request, menu_type='tournament_main'):
    token = get_token_from_header(request)
    print("tournament_main is loading")
    if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
    else:
        menu = modify_json_menu(menu_type, token)
        menu = tournament_select_fill(menu)

    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

# Creation form of tournament

def tournament_create(request, menu_type='tournament_create'):
    token = get_token_from_header(request)
    if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
    else:
        menu = modify_json_menu(menu_type, token)

    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

# Processing of the form submitted at tournament_create()
#   Creates an instance/s of: Tournament & Participants & Games & Players

def tournament_create_check(request, menu_type='main'):
    token = get_token_from_header(request)

    data = json.loads(request.body)
    tournament_name = data.get("tournament_name")
    participants = data.get("players")
    players = participants

    if len(players) % 2:
        players.append(None)

    n = len(players)
    schedule = []

    for round in range(n - 1):
        round_matches = []
        for i in range(n // 2):
            if players[i] is not None and players[n - 1 - i] is not None:
                round_matches.append((players[i], players[n - 1 - i]))
        players.insert(1, players.pop())
        schedule.append(round_matches)

    print(schedule)

    tournament_db = Tournaments(name=tournament_name)
    tournament_db.save()

    for participant in participants:
        try:
            user = Users2.objects.get(username=participant)
            participant_db = Participants(player=user, tournament=tournament_db)
            participant_db.save()
        except Users2.DoesNotExist:
            print(f"User {participant} does not exist")
            continue

    for rounds in schedule:
        for matches in rounds:
            player1 = Users2.objects.get(username=matches[0])
            player2 = Users2.objects.get(username=matches[1])

            game_db = Games(tournament=tournament_db)
            game_db.save()
            player1_db = Players(player=player1, game=game_db)
            player1_db.save()
            player2_db = Players(player=player2, game=game_db)
            player2_db.save()
    
    
    if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
    else:
        menu = modify_json_menu(menu_type, token)

    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

# Load the selected tournament (selected in tournament_main/initial page of tournament)

def tournament_select(request, menu_type='tournament_select'):
    token = get_token_from_header(request)
    if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
    else:
        data = json.loads(request.body)
        tournament_name = data.get("tournament_name")
        participants = Participants.objects.filter(tournament__name=tournament_name).order_by('-points')
        print(participants)
        menu = modify_json_menu(menu_type, token)
        response_data = tournament_select_page_fill(menu, participants)

    if menu is not None:
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

# Prepare game to be played

def tournament_game_check(request, menu_type="local_game"):
    token = get_token_from_header(request)

    data = json.loads(request.body)

    # if (token == None) or (not validate_token(token)):
    menu = copy.deepcopy(MENU_DATA.get(menu_type))
    # else:
    #     menu = None

    print(data)
    # response_data = {'player1': player1, 'player2': player2, 'player1_id': player1_db.id, 'player2_id': player2_db.id}


    players = Players.objects.filter(game=data['game_id'])
    print(players[0].player.username)
    print(players)

    response_data = {'menu': menu, 'game_id': data['game_id'], 'player1': players[0].player.username, 'player1_id': players[0].id, 'player2': players[1].player.username, 'player2_id': players[1].id}

    if menu is not None:
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

# Check tournament game results, manipulate database
#   In case of last tournament game, save results to blockchain.

def close_tournament_game(request, menu_type='main'):
    try:
        token = get_token_from_header(request)

        data = json.loads(request.body)
        player1 = data.get('player1')
        player2 = data.get('player2')
        game_id = data.get('game').get('game_id')
        print(game_id)
        game_db = Games.objects.get(id=game_id)

        if player1.get('status') == 'winner':
            player1_db = Users2.objects.get(username=player1.get('name'))
            player1_db.wins += 1
            player1_db.save()

            player2_db = Users2.objects.get(username=player2.get('name'))
            player2_db.losses += 1
            player2_db.save()

            player_id = player1.get('id')
            if player_id is None:
                return JsonResponse({'error': 'Player 1 ID not provided'}, status=400)

            try:
                player = Players.objects.get(id=player_id)
                game = Games.objects.get(id=player.game.id)
                game.result = player1.get('name')
                game.save()

                # Update Participants.points for the winner
                participant = Participants.objects.get(player=player1_db, tournament=game.tournament)
                participant.points += 1
                participant.save()
            except Players.DoesNotExist:
                return JsonResponse({'error': 'Player 1 not found'}, status=404)
            except Games.DoesNotExist:
                return JsonResponse({'error': 'Game not found'}, status=404)
            except Participants.DoesNotExist:
                return JsonResponse({'error': 'Participant not found'}, status=404)

        else:
            player1_db = Users2.objects.get(username=player1.get('name'))
            player1_db.losses += 1
            player1_db.save()

            player2_db = Users2.objects.get(username=player2.get('name'))
            player2_db.wins += 1
            player2_db.save()

            player_id = player1.get('id')
            if player_id is None:
                return JsonResponse({'error': 'Player 1 ID not provided'}, status=400)

            try:
                player = Players.objects.get(id=player_id)
                game = Games.objects.get(id=player.game.id)
                game.result = player2.get('name')
                game.save()

                # Update Participants.points for the winner
                participant = Participants.objects.get(player=player2_db, tournament=game.tournament)
                participant.points += 1
                participant.save()
            except Players.DoesNotExist:
                return JsonResponse({'error': 'Player 1 not found'}, status=404)
            except Games.DoesNotExist:
                return JsonResponse({'error': 'Game not found'}, status=404)
            except Participants.DoesNotExist:
                return JsonResponse({'error': 'Participant not found'}, status=404)

        #TBC
        first_game_with_empty_result = Games.objects.filter(
            (Q(result__isnull=True) | Q(result='Not Set')) & Q(tournament_id=game.tournament)
        ).order_by('id').first()

        if not first_game_with_empty_result:
            tournament = Tournaments.objects.get(id=game.tournament.id)
            tournament_winner = Participants.objects.filter(tournament=tournament.id).order_by('-points').first()
            if tournament_winner:
                add_tournament_to_blockchain(tournament.name, tournament_winner.player.username)

        # Determine the menu based on the token
        if (token is None) or (not validate_token(token)):
            menu = copy.deepcopy(MENU_DATA.get(menu_type))
        else:
            menu = modify_json_menu(menu_type, token)

        # Return the menu if found, else return an error response
        if menu is not None:
            return JsonResponse(menu)
        else:
            return JsonResponse({'error': 'Menu type not found'}, status=404)

    except Users2.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


    # AUTHENTICATION

# Load Login Form

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

# Load Registration Form

def register(request, warning: str = None, menu_type='register'):
    token = get_token_from_header(request)
    if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
        avatars = Avatar.objects.all()
        print(avatars)
        for avatar in avatars:
            menu['menuItems'][0]['content'][0]['content'][3]['content'][1]['content'].append({
                'type': 'option',
                'value': avatar.name,
                'text': avatar.name
        })
    else:
        menu = modify_json_menu(menu_type, token)
        avatars = Avatar.objects.all()
        print(avatars)
        for avatar in avatars:
            menu['menuItems'][0]['content'][0]['content'][2]['content'][1]['content'].append({
                'type': 'option',
                'value': avatar.name,
                'text': avatar.name
            })

    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

# Process Data from Registration Form

def registration_check(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(request.body)
            username = data.get('username')
            if username == '': raise Exception("username_not_specified")
            password = data.get('password')
            if password == '': raise Exception("password_not_specified")
            pre = "https://127.0.0.1:8000/static/images/"
            print(data.get("avatar"))
            avatar = pre + data.get('avatar')
            print(avatar)
            email = data.get('email')
            print(email)
            twofa = data.get('twofa')
            print(twofa)
            new_user = Users2(username=username, email=email, wins=0, losses=0, avatarDirect=avatar, allow_otp=twofa)
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

# Generate One Time Password

def generate_otp():
    return str(random.randint(100000, 999999))

# Process Data From Login Form

import traceback

@csrf_exempt
def login_check(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(data)
            print("PRINT THE LINE BEFORE")
            username = data.get('username')
            password = data.get('password')
            
            if not username or not password:
                return JsonResponse({'error': 'Username and password are required.'}, status=400)
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.allow_otp:
                    otp = generate_otp()
                    request.session['otp'] = otp
                    request.session['username'] = username
                    request.session['password'] = password
                    print(f"Your OTP is: {otp}")
                    
                    return JsonResponse({'status': 'otp_sent'})
                else:
                    login(request, user)
                    access_token = str(AccessToken.for_user(user))
                    response_data = modify_json_menu('main', access_token)
                    
                    response = JsonResponse(response_data)
                    response.set_cookie(
                        'access_token', access_token, httponly=True, secure=True, samesite='Strict'
                    )
                    
                    return response
            else:
                return JsonResponse({'error': 'Invalid username or password'}, status=401)
        except Exception as e:
            print("Exception occurred:", e)
            traceback.print_exc()
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST method is allowed.'}, status=405)

# Load OTP View if Two-Factor is enabled for user.

@csrf_exempt
def verify_otp_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            otp_input = data.get('otp')
            
            if otp_input == request.session.get('otp'):
                # OTP is correct, log the user in
                username = request.session.get('username')
                password = request.session.get('password')
                
                user = authenticate(request, username=username, password=password)
                
                if user is not None:
                    login(request, user)
                    access_token = str(AccessToken.for_user(user))
                    
                    # Assuming modify_json_menu requires a token and modifies the menu accordingly
                    response_data = modify_json_menu('main', access_token)
                    
                    response = JsonResponse(response_data)
                    response.set_cookie(
                        'access_token', access_token, httponly=True, secure=True, samesite='Strict'
                    )
                    
                    # Clear session data
                    request.session.pop('otp', None)
                    request.session.pop('username', None)
                    request.session.pop('password', None)
                    
                    return response
            return JsonResponse({'error': 'Invalid OTP'}, status=401)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST method is allowed.'}, status=405)
# def index(request):
#     return render(request, "/", {})

def logout(request):
    if request.method == "POST":
        try:
            response = JsonResponse({'message': 'Logged out successfully'})
            response.delete_cookie('access_token')
            response.delete_cookie('refresh_token')
            return response
        except Exception as e:
            pass

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})

# views.py

# views.py

import base64
import os
from pathlib import Path
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Upload File to server in the registration form

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        file_name = data.get('fileName')
        file_type = data.get('fileType')
        file_data = data.get('fileData')

        if not file_name or not file_data:
            return JsonResponse({'error': 'Invalid file data'}, status=400)

        # Decode the base64 file data
        file_content = base64.b64decode(file_data)

        # Construct the file path
        static_images_dir = Path(settings.BASE_DIR) / 'static' / 'images'
        file_path = static_images_dir / file_name

        # Ensure the directory exists
        os.makedirs(static_images_dir, exist_ok=True)

        # Write the file
        with open(file_path, 'wb') as f:
            f.write(file_content)

        return JsonResponse({'message': 'File uploaded successfully', 'file_path': str(file_path)})
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)

# Load User Settings

def settings(request, menu_type='settings'):
    token = get_token_from_header(request)
    user = get_user_from_token(token)
    if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
    else:
        menu = modify_json_menu(menu_type, token)
        avatars = Avatar.objects.all()
        print(avatars)
        i = 0
        for avatar in avatars:
            menu['menuItems'][0]['content'][1]['content'][1]['content'].append({
                'type': 'option',
                'value': avatar.name,
                'text': avatar.name
            })

            if avatar.name == user.avatarDirect.rsplit('/', 1)[1]:
                menu['menuItems'][0]['content'][1]['content'][1]['content'][1]['selected'] = user.avatarDirect.rsplit('/', 1)[1]
            i = i + 1

        menu['menuItems'][0]['content'][0]['value'] = user.username

        # menu['menuItems'][0]['content'][0]['content'][1]['selected'] = user.avatarDirect.rsplit('/', 1)[1]
        print(menu)
        # menu['menuItems'][0]['content'][0]['content'][1]['content']

    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

# In Settings, reset user statistics

def delete_user_stats(request, menu_type='main'):
    token = get_token_from_header(request)
    user = get_user_from_token(token)

    user.wins = 0
    user.losses = 0
    user.save()

    if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
    else:
        menu = modify_json_menu(menu_type, token)

    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

# In Settings, save changes to user data

def save_changes(request, menu_type='main'):
    token = get_token_from_header(request)
    user = get_user_from_token(token)

    try:
        data = json.loads(request.body)
        username = data.get('username')
        avatar = data.get('avatar')
        pre = "https://127.0.0.1:8000/static/images/"
        print(data.get("avatar"))
        avatar = pre + data.get('avatar')

        user.username = username
        print(avatar)
        user.avatarDirect = avatar
        user.save()
    except Exception as e:
        pass

    if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
    else:
        menu = modify_json_menu(menu_type, token)

    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)