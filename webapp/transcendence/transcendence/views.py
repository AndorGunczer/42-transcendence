# Functions as to what the server should do upon requests at specific urls

from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from transcendence.models import Users2, Tournaments, Participants, Players, Games, Avatar, Friends, Messages
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
import copy
from django.middleware.csrf import get_token
import json
import random
from transcendence.web3_utils import add_tournament, add_participant, increment_score, set_winner, get_tournament_count, get_tournament, get_participant_score, get_participant_list, get_tournament_index_by_name
from .menus import MENU_DATA
from django.db.models import Q

import os
from dotenv import load_dotenv

# Importing .ENV

load_dotenv()

# Access environment variables
SMTP_SERVER = os.getenv('SMTP_SERVER')
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
EMAIL_PW = os.getenv('EMAIL_PW')


# Initial Load of Site

class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh_token')
        if not refresh_token:
            return JsonResponse({"error": "Refresh token missing"}, status=401)
            # return JsonResponse({"message": "Refresh token missing"}, status=200)

        request.data['refresh'] = refresh_token
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            data = response.data
            response = JsonResponse({"message": "Token refreshed"}, status=200)
            response.set_cookie(
                'access_token', data['access'], httponly=True, secure=True, samesite='Strict'
            )
        return response

# Testing
@csrf_exempt
def simulate_error(request):
    return JsonResponse({'error': 'Testing is successful'}, status=500)


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
    menu['headerItems'][0]['content'][1]['identifier'] = 'user'
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
        del menu['menuItems'][3]

        menu['menuItems'].append({
                'id': 4,
                'type': 'button',
                'class': 'col-md-12 mt-2 p-3 h-50 w-25 mb-4 rounded bg-secondary bg-gradient text-white',
                'text': 'MATCH HISTORY',
                'onclick': 'loadHistory()'
            })

    # Add Friendlist
    menu['menuItems'].append({
        'id': len(menu['menuItems']),
        'type': 'div',
        'class': 'h-75 w-25 position-fixed top-25 end-0 border border-white overflow-scroll',
        'content': [
            {
                # add friend
                'type': 'div',
                'class': 'd-flex flex-column',
                'content': [
                    {
                        'type': 'input',
                        'inputType': 'text',
                        'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                        'placeholder': 'add a friend...',
                        'identifier': 'friend-name',
                        'name': 'friend',
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button col-md-12 mt-2 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'text': 'ADD FRIEND',
                        'onclick': 'chatSocket.sendFriendRequest(event)',
                    }
                ]
            },
            {
                # friend request list
                'type': 'div',
                'class': 'd-flex flex-column',
                'content': [
                    {
                        'type': 'div',
                        'identifier': 'friend-requests',
                        'class': 'd-flex flex-column',
                        'content': [
                            {
                                'type': 'h3',
                                'class': 'text-white',
                                'text': 'Friend Requests'
                            },
                        ]
                    },
                ]
            },
            {
                # friendlist
                'type': 'div',
                'class': 'd-flex flex-column',
                'content': [
                    {
                        'type': 'div',
                        'identifier': 'friends',
                        'class': 'd-flex flex-column',
                        'content': [
                            {
                                'type': 'h3',
                                'class': 'text-white',
                                'text': 'Friends'
                            },
                        ]
                    },
                ]
            }
        ]
    })

    friend_requests_div = menu['menuItems'][len(menu['menuItems'])-1]['content'][1]['content']
    friends_div = menu['menuItems'][len(menu['menuItems'])-1]['content'][2]['content']

    friend_requests_db = Friends.objects.filter(
        Q(friend1__username=user.username) | Q(friend2__username=user.username),
        state="pending"
    )

    friends_db = Friends.objects.filter(
        Q(friend1__username=user.username) | Q(friend2__username=user.username),
        state="accepted"
    )

    for request in friend_requests_db:
        if (request.friend2.username == user.username):
            friend_requests_div.append({
                'type': 'div',
                'class': 'd-flex flex-column',
                'content': [
                    {
                        'type': 'p',
                        'class': 'text-white m-3',
                        'text': f"new friend request from {request.friend1.username if user.username == request.friend2.username else request.friend2.username}",
                    },
                    {
                        'type': 'div',
                        'class': 'd-flex flex-column',
                        'content': [
                            {
                                'type': 'button',
                                'class': 'rounded bg-secondary bg-gradient text-white',
                                'onclick': f"chatSocket.acceptFriendRequest(this.id)",
                                'identifier': f"{request.friend1.username if user.username == request.friend2.username else request.friend2.username}",
                                'text': 'ACCEPT'
                            },
                            {
                                'type': 'button',
                                'class': 'rounded bg-secondary bg-gradient text-white',
                                'onclick': f"chatSocket.declineFriendRequest(this.id)",
                                'identifier': f"{request.friend1.username if user.username == request.friend2.username else request.friend2.username}",
                                'text': 'DECLINE'
                            }
                        ]
                    }
                ]
            })

    # Assume you have a variable indicating the current page

    for friend in friends_db:
        this_friend = friend.friend1 if user.username == friend.friend2.username else friend.friend2
        friend_name = this_friend.username
        is_online = "Online" if this_friend.is_online else "Offline"


        print(f'''???????????????????????????????
        friend_name: {friend_name}
        friend.friend1.username: {friend.friend1.username}
        friend.friend2.username: {friend.friend2.username}
        is_online: {is_online}''')

        # Base content for each friend
        content = [
            {
                'type': 'p',
                'class': 'text-white m-3',
                'text': friend_name,
                'translate': 'no'  # Prevent translation
            },
            {
                'type': 'p',
                'class': 'text-white m-1 is_online',
                'text': is_online,
                'translate': 'no'  # Prevent translation if needed
            },
            {
                'type': 'div',
                'class': 'd-flex flex-column',
                'content': [
                    {
                        'type': 'button',
                        'class': 'rounded bg-secondary bg-gradient text-white',
                        'onclick': f"chat(this.id)",
                        'identifier': friend_name,
                        'text': 'CHAT',
                        'translate': 'no'  # Prevent translation if needed
                    },
                ]
            }
        ]

        # Conditionally add the "Invite" button if the current page is "tournament_select"
        if menu_type == "tournament_create":
            content[2]['content'].append({
                'type': 'button',
                'class': 'rounded bg-secondary bg-gradient text-white',
                'onclick': f"validateAndAddToTournament(this.id)",
                'identifier': friend_name,
                'text': 'INVITE',
                'translate': 'no'  # Prevent translation if needed
            })

        friends_div.append({
            'type': 'div',
            'class': 'd-flex flex-column',
            'content': content
        })


    menu['menuItems'].append({
        'type': 'div',
        'class': 'position-fixed d-flex flex-row bottom-0 start-0 h-25 w-100 pe-none',
        'identifier': 'chat-container',
        'content': [

        ]
    })


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



def tournament_select_page_fill(menu, participants, tournament_name):
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
        'class': 'w-100 d-flex flex-column justify-content-center align-items-center',
        'content': [
            {
                'type': 'thead',
                'class': 'thead-dark text-white w-100 d-flex flex-row justify-content-center gap-4',
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

    table = menu['menuItems'][0]['content'][0]['content'][0]['content']

    for i,participant in enumerate(participants.keys()):
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
                    'text': participant,
                },
                {
                    'type': 'td',
                    'class': 'text-white',
                    'text': f'{participants[participant]}'
                }
            ]
        })

    if participants:
        tournament = Tournaments.objects.get(name=tournament_name)


        # tournament_id = (Participants.objects.get(player=list(participants.items())[0])).tournament # participants[0].tournament_id # (original)
        # print(f'tournament id: {tournament_id}') get_tournament_index_by_name(game_db.tournament.name)

        # Correctly formed query to get the first Game where result is either None or 'Not Set' and matches the given tournament_id
        first_game_with_empty_result = Games.objects.filter(
            (Q(result__isnull=True) | Q(result='Not Set')) & Q(tournament_id=tournament.id)
        ).order_by('id').first()


        if first_game_with_empty_result:
            players_of_game = Players.objects.filter(game=first_game_with_empty_result.id)
            player1 = None
            player2 = None
            # player1 TO BE CONTINUED
            if players_of_game[0].player:
                player1 = players_of_game[0].player.username
            else:
                player1 = players_of_game[0].guest_name

            if players_of_game[1].player:
                player2 = players_of_game[1].player.username
            else:
                player2 = players_of_game[1].guest_name

            if len(players_of_game) >= 2:
                menu['menuItems'][0]['content'][1]['text'] = f'{player1} vs {player2}'
            else:
                # Display winner of tournament (blockchain)
                top_participant = get_tournament(get_tournament_index_by_name(tournament.name))[1]
                if top_participant:
                    menu['menuItems'][0]['content'][1]['text'] = f'Winner: {top_participant}'
                else:
                    menu['menuItems'][0]['content'][1]['text'] = 'Winner: Unknown'
        else:
            top_participant = get_tournament(get_tournament_index_by_name(tournament.name))[1]
            if top_participant:
                menu['menuItems'][0]['content'][1]['text'] = f'Winner: {top_participant}'
            else:
                menu['menuItems'][0]['content'][1]['text'] = 'Winner: Unknown'
            del menu['menuItems'][0]['content'][2]
    else:
        menu['menuItems'][0]['content'][1]['text'] = 'No participants found'

    print('tournament_select_page_fill() called')
    return {'headerItems': menu['headerItems'], 'menuItems': menu['menuItems'], 'id': menu['id'], 'game': first_game_with_empty_result.id if first_game_with_empty_result else None}


# Consumer Interaction

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def notify_user(user_id, message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{user_id}",  # Group name
        {
            "type": "tournament_broadcast",
            "message": message,
        }
    )

# VIEW FUNCTIONS

# Initial Website Load

def index(request):
    token = get_token_from_header(request)
    if (token == None) or (not validate_token(token)):
        obj = {
            'username': 'Guest',
            'wins': 'None',
            'losses': 'None',
            'authenticated': 'False'
        }
        response = render(request, 'menu_general/index.html', obj)
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response
    else:
        try:
            user = get_user_from_token(token)
            obj = {
                'username': user.username,
                'wins': user.wins,
                'losses': user.losses,
                'authenticated': 'True'
            }
            print(obj)
            return render(request, 'menu_general/index.html', obj)
        except Users2.DoesNotExist:
            response = render(request, 'menu_general/index.html', {
                'username': 'Guest',
                'wins': 'None',
                'losses': 'None',
                'authenticated': 'False'
            })
            response.delete_cookie('access_token')
            response.delete_cookie('refresh_token')
            return response

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

def match_history(request, menu_type='match_history'):
    token = get_token_from_header(request)
    if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
    else:
        user = get_user_from_token(token)
        menu = modify_json_menu(menu_type, token)
        menu = match_history_fill(menu, user)
    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

def match_history_fill(menu, user):
    match_history = Games.objects.filter(players__player=user).order_by('-date_of_game')
    print(match_history)

    menu['menuItems'][0]['content'].append({
        'type': 'table',
        'class': 'w-100 d-flex flex-column justify-content-center align-items-center',
        'content': [
            {
                'type': 'thead',
                'class': 'thead-dark text-white w-100 d-flex flex-row justify-content-center gap-4',
                'content': [
                    {
                        'type': 'td',
                        'class': 'text-white',
                        'text': 'Date'
                    },
                    {
                        'type': 'td',
                        'class': 'text-white',
                        'text': 'Opponent'
                    },
                    {
                        'type': 'td',
                        'class': 'text-white',
                        'text': f'Winner'
                    }
                ]
            }
        ]
    })

    table = menu['menuItems'][0]['content'][0]['content']

    for match in match_history:
        opponent = (Players.objects.filter(game=match).exclude(player=user))[0]
        opponent_name = None

        if opponent.player is not None:
            opponent_name = opponent.player.username
            print(f"Opponent: {opponent.player.username}")
        else:
            opponent_name = opponent.guest_name
            print(f"Opponent: {opponent.guest_name}")

        table.append({
            'type': 'tr',
            'class': 'participant text-white',
            'content': [
                {
                    'type': 'td',
                    'class': 'text-white',
                    'text': f'{match.date_of_game}'
                },
                {
                    'type': 'td',
                    'class': 'text-white',
                    'text': opponent_name,
                },
                {
                    'type': 'td',
                    'class': 'text-white',
                    'text': f'{match.result}'
                }
            ]
        })

    return menu

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

from rest_framework.response import Response
from rest_framework.decorators import api_view
from transcendence.models import Games, Users2, Players
from transcendence.serializers import LocalGameRequestSerializer
import copy

@api_view(['POST'])
def local_check(request, menu_type='local_game'):
    token = get_token_from_header(request)

    # Deserialize the request data
    serializer = LocalGameRequestSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'error': 'Invalid data'}, status=400)

    player1 = serializer.validated_data['player1']
    player2 = serializer.validated_data['player2']

    # Create a new game instance
    game_db = Games()
    game_db.save()

    # Try to create or assign player1 to the game
    try:
        player1_db = Players(player=Users2.objects.get(username=player1), game=game_db)
    except Users2.DoesNotExist:
        player1_db = Players(game=game_db, guest_name=player1)
    player1_db.save()

    # Try to create or assign player2 to the game
    try:
        player2_db = Players(player=Users2.objects.get(username=player2), game=game_db)
    except Users2.DoesNotExist:
        player2_db = Players(game=game_db, guest_name=player2)
    player2_db.save()

    # Prepare the response data in the required format
    response_data = {
        'player1': player1,
        'player2': player2,
        'player1_id': player1_db.id,
        'player2_id': player2_db.id
    }

    # Check token and modify the menu if necessary
    menu = copy.deepcopy(MENU_DATA.get(menu_type))  # You can replace this with actual menu handling logic

    if menu is not None:
        return Response(response_data, status=200)
    else:
        return Response({'error': 'Menu type not found'}, status=404)

# Database Manipulation based on the results of Local Game

def close_local(request, menu_type='main'):
    try:
        token = get_token_from_header(request)

        data = json.loads(request.body)
        player1 = data.get('player1')
        player2 = data.get('player2')
        # game_id = player1.get('name').get('game')

        if player1.get('status') == 'winner':
            try:
                player1_db = Users2.objects.get(username=player1.get('name'))
                player1_db.wins += 1
                player1_db.save()
            except Users2.DoesNotExist:
                print("User is not found, probably a guest user is used")

            try:
                player2_db = Users2.objects.get(username=player2.get('name'))
                player2_db.losses += 1
                player2_db.save()
            except Users2.DoesNotExist:
                print("User is not found, probably a guest user is used")

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
            try:
                player1_db = Users2.objects.get(username=player1.get('name'))
                player1_db.losses += 1
                player1_db.save()
            except Users2.DoesNotExist:
                print("User is not found, probably a guest user is used")

            try:
                player2_db = Users2.objects.get(username=player2.get('name'))
                player2_db.wins += 1
                player2_db.save()
            except Users2.DoesNotExist:
                print("User is not found, probably a guest user is used")

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

from rest_framework.response import Response
from rest_framework.decorators import api_view
from transcendence.models import Tournaments, Users2, Participants, Games, Players
from transcendence.serializers import TournamentCreateSerializer
import copy

@api_view(['POST'])
def tournament_create_check(request, menu_type='main'):
    token = get_token_from_header(request)

    # Deserialize and validate the request data
    serializer = TournamentCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'error': 'Invalid data'}, status=400)

    tournament_name = serializer.validated_data['tournament_name']
    participants = serializer.validated_data['players']
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

    # Create Tournament in the Database
    tournament_db = Tournaments(name=tournament_name)
    try:
        tournament_db.save()
    except Exception as e:
        return JsonResponse({'error': 'Tournament is already created.'}, status=400)

    # Create Tournament on the Blockchain
    receipt = add_tournament(tournament_name, "No Winner Yet")
    print(f"addTournament transaction successful with hash: {receipt.transactionHash.hex()}")

    # Add participants
    for participant in participants:
        if participant is None:
            continue
        try:
            print(f'try participant: {participant}')
            user = Users2.objects.get(username=participant)
            # Create Participants in Database
            participant_db = Participants(player=user, tournament=tournament_db)
            participant_db.save()
            # Add Participants to Blockchain
            receipt = add_participant(get_tournament_index_by_name(tournament_name), user.username)
            print(f"addParticipant transaction successful with hash: {receipt.transactionHash.hex()}")
        except Users2.DoesNotExist:
            print(f'except participant: {participant}')
            user = participant
            participant_db = Participants(tournament=tournament_db, guest_name=user)
            participant_db.save()
            receipt = add_participant(get_tournament_index_by_name(tournament_name), user)
            print(f"addParticipant transaction successful with hash: {receipt.transactionHash.hex()}")
            continue

    # Schedule matches
    for rounds in schedule:
        for matches in rounds:
            game_db = Games(tournament=tournament_db)
            game_db.save()

            player1 = matches[0]
            player2 = matches[1]

            try:
                player1_db = Players(player=Users2.objects.get(username=player1), game=game_db)
                player1_db.save()
            except Users2.DoesNotExist:
                player1_db = Players(game=game_db, guest_name=player1)
                player1_db.save()

            try:
                player2_db = Players(player=Users2.objects.get(username=player2), game=game_db)
                player2_db.save()
            except Users2.DoesNotExist:
                player2_db = Players(game=game_db, guest_name=player2)
                player2_db.save()

    #TBC
    first_game_with_empty_result = Games.objects.filter(
        (Q(result__isnull=True) | Q(result='Not Set')) & Q(tournament_id=tournament_db.id)
    ).order_by('id').first()

    if first_game_with_empty_result:
        registered_players = Players.objects.filter(game_id=first_game_with_empty_result.id).exclude(player_id=None)
        for player in registered_players:
            notify_user(player.player_id, "Next Tournament Game is Yours!")

    # Token and menu handling
    if (token is None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
    else:
        menu = modify_json_menu(menu_type, token)

    if menu is not None:
        return Response(menu)
    else:
        return Response({'error': 'Menu type not found'}, status=404)

# Load the selected tournament (selected in tournament_main/initial page of tournament)

def tournament_select(request, menu_type='tournament_select'):
    token = get_token_from_header(request)
    if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
    else:
        data = json.loads(request.body)
        tournament_name = data.get("tournament_name")
        # REWORK WITH BLOCKCHAIN

        # Database Implementation
        participants = Participants.objects.filter(tournament__name=tournament_name).order_by('-points')
        print(participants)

        # Blockchain Implementation
        participants_b = {}
        try:
            index = get_tournament_index_by_name(tournament_name)
        except Exception as e:
            return JsonResponse({'error': 'Tournament not created in the Blockchain (Did you restart the container?)'}, status=404)
        p_list = get_participant_list(index)

        for participant in p_list:
            print("ROUND")
            participants_b[participant] = get_participant_score(index, participant)

        # Sort Dictionary in Reverse order based on Values

        participants_b = {key: val for key, val in sorted(participants_b.items(), key = lambda ele: ele[1], reverse = True)}

        print(participants_b)

        menu = modify_json_menu(menu_type, token)
        response_data = tournament_select_page_fill(menu, participants_b, tournament_name)

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
    player1 = ""
    player2 = ""
    if players[0].player:
        player1 = players[0].player.username
    else:
        player1 = players[0].guest_name

    if players[1].player:
        player2 = players[1].player.username
    else:
        player2 = players[1].guest_name

    # print(players[0].player.username)
    print(players)

    response_data = {'menu': menu, 'game_id': data['game_id'], 'player1': player1, 'player1_id': players[0].id, 'player2': player2, 'player2_id': players[1].id}

    if menu is not None:
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

# Check tournament game results, manipulate database
#   In case of last tournament game, save results to blockchain.

def close_tournament_game(request, menu_type='main'):
    try:
        token = get_token_from_header(request)

        # database

        data = json.loads(request.body)
        player1 = data.get('player1')
        player2 = data.get('player2')
        game_id = data.get('game').get('game_id')
        print(game_id)
        game_db = Games.objects.get(id=game_id)
        tournament = game_db.tournament

        # blockchain
        # print(game_db.tournament.name)
        # blockchain_tournament = get_tournament_index_by_name(game_db.tournament.name)
        # print(blockchain_tournament)

        # blockchain end

        if player1.get('status') == 'winner':
            try:
                player1_db = Users2.objects.get(username=player1.get('name'))
                player1_db.wins += 1
                player1_db.save()
            except Users2.DoesNotExist:
                print("User is not found, probably a guest user is used")

            try:
                player2_db = Users2.objects.get(username=player2.get('name'))
                player2_db.losses += 1
                player2_db.save()
            except Users2.DoesNotExist:
                print("User is not found, probably a guest user is used")

            player_id = player1.get('id')
            if player_id is None:
                return JsonResponse({'error': 'Player 1 ID not provided'}, status=400)

            # Update Winner in the Game
            game_db.result = player1.get('name')
            game_db.save()

            # Update Participants.points for the winner in Database
            try:
                # Try to retrieve a Users2 object using the identifier (assuming it's a username)
                user = Users2.objects.get(username=player1.get('name'))
                player = user
                participant = Participants.objects.get(player=player, tournament=tournament)

                if participant:
                    participant.points += 1
                    participant.save()
                    # Update Participants.points for the winner on the Blockchain
                    receipt = increment_score(get_tournament_index_by_name(game_db.tournament.name), participant.player.username, 1)
                    print(f"incrementScore transaction successful with hash: {receipt.transactionHash.hex()}")

            except Users2.DoesNotExist:
                # If the user doesn't exist, try to find the participant by guest name
                participant = Participants.objects.get(guest_name=player1.get('name'), tournament=tournament)

                if participant:
                    participant.points += 1
                    participant.save()
                    # Update Participants.points for the winner on the Blockchain
                    receipt = increment_score(get_tournament_index_by_name(game_db.tournament.name), participant.guest_name, 1)
                    print(f"incrementScore transaction successful with hash: {receipt.transactionHash.hex()}")

            except Players.DoesNotExist:
                return JsonResponse({'error': 'Player 1 not found'}, status=404)
            except Games.DoesNotExist:
                return JsonResponse({'error': 'Game not found'}, status=404)
            except Participants.DoesNotExist:
                return JsonResponse({'error': 'Participant not found'}, status=404)

        else:
            try:
                player1_db = Users2.objects.get(username=player1.get('name'))
                player1_db.losses += 1
                player1_db.save()
            except Users2.DoesNotExist:
                print("User is not found, probably a guest user is used")

            try:
                player2_db = Users2.objects.get(username=player2.get('name'))
                player2_db.wins += 1
                player2_db.save()
            except Users2.DoesNotExist:
                print("User is not found, probably a guest user is used")

            player_id = player1.get('id')
            if player_id is None:
                return JsonResponse({'error': 'Player 1 ID not provided'}, status=400)

            game_db.result = player2.get('name')
            game_db.save()

            # Update Participants.points for the winner in Database
            try:
                # Try to retrieve a Users2 object using the identifier (assuming it's a username)
                user = Users2.objects.get(username=player2.get('name'))
                player = user
                participant = Participants.objects.get(player=player, tournament=tournament)

                if participant:
                    participant.points += 1
                    participant.save()
                    # Update Participants.points for the winner on the Blockchain
                    receipt = increment_score(get_tournament_index_by_name(game_db.tournament.name), participant.player.username, 1)
                    print(f"incrementScore transaction successful with hash: {receipt.transactionHash.hex()}")

            except Users2.DoesNotExist:
                # If the user doesn't exist, try to find the participant by guest name
                participant = Participants.objects.get(guest_name=player2.get('name'), tournament=tournament)

                if participant:
                    participant.points += 1
                    participant.save()
                    # Update Participants.points for the winner on the Blockchain
                    receipt = increment_score(get_tournament_index_by_name(game_db.tournament.name), participant.guest_name, 1)
                    print(f"incrementScore transaction successful with hash: {receipt.transactionHash.hex()}")
            except Players.DoesNotExist:
                return JsonResponse({'error': 'Player 1 not found'}, status=404)
            except Games.DoesNotExist:
                return JsonResponse({'error': 'Game not found'}, status=404)
            except Participants.DoesNotExist:
                return JsonResponse({'error': 'Participant not found'}, status=404)

        #TBC
        first_game_with_empty_result = Games.objects.filter(
            (Q(result__isnull=True) | Q(result='Not Set')) & Q(tournament_id=game_db.tournament)
        ).order_by('id').first()

        if not first_game_with_empty_result:
            tournament = Tournaments.objects.get(id=game_db.tournament.id)
            tournament_winner = Participants.objects.filter(tournament=tournament.id).order_by('-points').first()
            # Set Tournament Winner on the Blockchain
            try:
                set_winner(get_tournament_index_by_name(game_db.tournament.name), tournament_winner.player.username)
            except:
                set_winner(get_tournament_index_by_name(game_db.tournament.name), tournament_winner.guest_name)
        else:
            registered_players = Players.objects.filter(game_id=first_game_with_empty_result.id).exclude(player_id=None)
            for player in registered_players:
                notify_user(player.player_id, "Next Tournament Game is Yours!")




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

# def registration_check(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             print(request.body)
#             username = data.get('username')
#             if username == '': raise Exception("username_not_specified")
#             password = data.get('password')
#             if password == '': raise Exception("password_not_specified")
#             pre = "https://localhost/static/images/"
#             print(data.get("avatar"))
#             avatar = pre + data.get('avatar')
#             print(avatar)
#             email = data.get('email')
#             print(email)
#             twofa = data.get('twofa')
#             print(twofa)
#             new_user = Users2(username=username, email=email, wins=0, losses=0, avatarDirect=avatar, allow_otp=twofa)
#             new_user.set_password(password)
#             new_user.save()
#             # Users.objects.create(username=username, password=Users.make_password(password), wins=0, losses=0, games=None)
#             return JsonResponse(MENU_DATA.get('main'))
#         except Exception as e:
#             warning = e
#             print(warning)
#             return JsonResponse({'error': f'Username {username} already taken'}, status=404)

#     else:
#         return JsonResponse(MENU_DATA.get('register'))

from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer, LoginSerializer, UserUpdateSerializer

@api_view(['POST'])
def registration_check(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        try:
            # Process the validated data
            data = serializer.validated_data
            # Create the user or any other processing
            new_user = Users2(
                username=data['username'],
                email=data['email'],
                wins=0,
                losses=0,
                avatarDirect="https://localhost/static/images/" + data['avatar'], #ENV
                allow_otp=data['twofa'],
            )
            new_user.set_password(data['password'])
            new_user.save()

            return JsonResponse(MENU_DATA.get('main'), status=200)
        except Exception as e:
            warning = e
            print(warning)
            username = serializer.validated_data['username']
            return JsonResponse({'error': f'Username {username} already taken'}, status=404)
    else:
        return JsonResponse({'errors': serializer.errors}, status=400)

# Generate One Time Password

def generate_otp():
    return str(random.randint(100000, 999999))

# Process Data From Login Form
import smtplib, ssl
import traceback

# @csrf_exempt
# def login_check(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             print(data)
#             print("PRINT THE LINE BEFORE")
#             username = data.get('username')
#             password = data.get('password')

#             if not username or not password:
#                 return JsonResponse({'error': 'Username and password are required.'}, status=400)

#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 if user.allow_otp:
#                     otp = generate_otp()
#                     request.session['otp'] = otp
#                     request.session['username'] = username
#                     request.session['password'] = password

#                     with open('output.txt', 'w') as file:
#                         file.write("2fa is active\n")

#                         try:
#                             # Configuration
#                             port = 465
#                             smtp_server = "smtp.gmail.com"
#                             sender_email = "ft.transcendence.2fa.42@gmail.com"
#                             receiver_email = user.email
#                             email_password = 'rwsv qnsl lqfa shic'
#                             message = f"""\
#                             Subject: Your OTP Code

#                             Your OTP code is {otp}."""
#                             context = ssl.create_default_context()

#                             file.write("Preparing to connect to the SMTP server\n")
#                             with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#                                 file.write("Connection to server was successful\n")
#                                 server.login(sender_email, email_password)
#                                 file.write("Login to the SMTP server was successful\n")
#                                 server.sendmail(sender_email, receiver_email, message)
#                                 file.write("Email sent successfully\n")

#                         except smtplib.SMTPException as e:
#                             file.write(f"SMTP error occurred: {e}\n")
#                             return JsonResponse({'error': 'Failed to send email'}, status=500)
#                         except Exception as e:
#                             file.write(f"An error occurred: {e}\n")
#                             return JsonResponse({'error': 'An unexpected error occurred'}, status=500)

#                     return JsonResponse({'status': 'otp_sent'})
#                 else:
#                     login(request, user)
#                     refresh = RefreshToken.for_user(user)

#                     refresh_token = str(refresh)
#                     access_token = str(refresh.access_token)

#                     # Assuming modify_json_menu requires a token and modifies the menu accordingly
#                     response_data = modify_json_menu('main', access_token)

#                     response = JsonResponse(response_data)
#                     response.set_cookie(
#                         'access_token', access_token, httponly=True, secure=True, samesite='Strict'
#                     )

#                     response.set_cookie(
#                         'refresh_token', refresh_token, httponly=True, secure=True, samesite='Strict'
#                     )

#                     # Clear session data
#                     request.session.pop('otp', None)
#                     request.session.pop('username', None)
#                     request.session.pop('password', None)
#                     return response

#             else:
#                 return JsonResponse({'error': 'Invalid username or password'}, status=401)
#         except Exception as e:
#             print("Exception occurred:", e)
#             traceback.print_exc()
#             return JsonResponse({'error': str(e)}, status=500)
#     else:
#         return JsonResponse({'error': 'Only POST method is allowed.'}, status=405)

from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
@csrf_exempt  # If needed, you can remove this if you're not using it for API
def login_check(request):
    # Use the LoginSerializer to validate the incoming data
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        # Extract validated data
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If user has OTP enabled, handle 2FA flow
            if user.allow_otp:
                otp = generate_otp()
                request.session['otp'] = otp
                request.session['username'] = username
                request.session['password'] = password

                try:
                    # Email configuration and sending the OTP code #ENV
                    port = 465
                    smtp_server = SMTP_SERVER
                    sender_email = SENDER_EMAIL
                    receiver_email = user.email
                    email_password = EMAIL_PW  # Should be stored securely
                    message = f"Subject: Your OTP Code\n\nYour OTP code is {otp}."
                    context = ssl.create_default_context()

                    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                        server.login(sender_email, email_password)
                        server.sendmail(sender_email, receiver_email, message)

                    return Response({'status': 'otp_sent'}, status=status.HTTP_200_OK)

                except smtplib.SMTPException as e:
                    return Response({'error': 'Failed to send email'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                except Exception as e:
                    return Response({'error': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # If OTP is not enabled, log the user in
            else:
                login(request, user)
                refresh = RefreshToken.for_user(user)

                refresh_token = str(refresh)
                access_token = str(refresh.access_token)

                # Assuming modify_json_menu customizes the menu for the logged-in user
                response_data = modify_json_menu('main', access_token)

                response = JsonResponse(response_data)
                response.set_cookie(
                    'access_token', access_token, httponly=True, secure=True, samesite='Strict'
                )
                response.set_cookie(
                    'refresh_token', refresh_token, httponly=True, secure=True, samesite='Strict'
                )

                # Clear sensitive session data
                request.session.pop('otp', None)
                request.session.pop('username', None)
                request.session.pop('password', None)

                return response

        else:
            # If authentication failed
            response = JsonResponse({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
            response.delete_cookie("access_token")
            response.delete_cookie("refresh_token")
            return response
    else:
        # If serializer validation failed
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

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
                    refresh = RefreshToken.for_user(user)

                    refresh_token = str(refresh)
                    access_token = str(refresh.access_token)

                    # Assuming modify_json_menu requires a token and modifies the menu accordingly
                    response_data = modify_json_menu('main', access_token)

                    response = JsonResponse(response_data)
                    response.set_cookie(
                        'access_token', access_token, httponly=True, secure=True, samesite='Strict'
                    )

                    response.set_cookie(
                        'refresh_token', refresh_token, httponly=True, secure=True, samesite='Strict'
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
            return JsonResponse({'error': str(e)}, status=404)

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
        static_images_dir = 'staticfiles/images' #ENV
        file_path = f'{static_images_dir}/{file_name}'

        # Ensure the directory exists
        os.makedirs(static_images_dir, exist_ok=True)

        # Write the file
        with open(file_path, 'wb') as f:
            f.write(file_content)

        Avatar.objects.create(
                    name=file_name,
                    path=file_path
                )

        return JsonResponse({'message': 'File uploaded successfully', 'file_path': str(file_path)})

    return JsonResponse({'error': 'Invalid request method'}, status=400)

# Load User Settings

def load_settings(request, menu_type='settings'):
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
            splitted_avatar = user.avatarDirect.rsplit('/', 1)[1]
            # print(f'splitted_avatar: ' + splitted_avatar + " name: " + avata.name + " | " + avatar.name == splitted_avatar)
            print(f'splitted_avatar: {splitted_avatar} name: {avatar.name} | {avatar.name == splitted_avatar}')
            if avatar.name == splitted_avatar:
                menu['menuItems'][0]['content'][1]['content'][1]['content'][i]['selected'] = splitted_avatar
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

# def save_changes(request, menu_type='main'):
#     token = get_token_from_header(request)
#     user = get_user_from_token(token)

#     try:
#         data = json.loads(request.body)
#         username = data.get('username')
#         avatar = data.get('avatar')
#         pre = "https://localhost/static/images/"
#         print(data.get("avatar"))
#         avatar = pre + data.get('avatar')

#         user.username = username
#         print(avatar)
#         user.avatarDirect = avatar
#         user.save()
#     except Exception as e:
#         pass

#     if (token == None) or (not validate_token(token)):
#         menu = copy.deepcopy(MENU_DATA.get(menu_type))
#     else:
#         menu = modify_json_menu(menu_type, token)

#     if menu is not None:
#         return JsonResponse(menu)
#     else:
#         return JsonResponse({'error': 'Menu type not found'}, status=404)

@api_view(['POST'])
def save_changes(request, menu_type='main'):
    # Get token and user
    token = get_token_from_header(request)
    user = get_user_from_token(token)

    # Use the serializer for validating incoming data
    serializer = UserUpdateSerializer(data=request.data)

    if serializer.is_valid():
        # Extract validated data
        username = serializer.validated_data.get('username')
        avatar = serializer.validated_data.get('avatar')

        # Update user information
        try:
            user.username = username

            # Prepend your custom URL prefix
            pre = "https://localhost/static/images/" #ENV
            avatar_url = pre + avatar
            user.avatarDirect = avatar_url

            user.save()

            print("DATABASE MODIFICATIONS HAVE BEEN SAVED")
            print(f'username: {user.username} avatarDirect: {user.avatarDirect}')

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Check token validation
        if token is None or not validate_token(token):
            menu = copy.deepcopy(MENU_DATA.get(menu_type))
        else:
            menu = modify_json_menu(menu_type, token)

        if menu is not None:
            return Response(menu, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Menu type not found'}, status=status.HTTP_404_NOT_FOUND)

    # If validation fails
    else:
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# FRIENDS

def fill_profile_with_user_data(menu, user):
    print(f"fill_profile_with_user_data: {user}")
    menu['menuItems'][0]['content'][1]['text'] = f'User: {user.username}'
    menu['menuItems'][0]['content'][2]['text'] = f'Wins: {user.wins}'
    menu['menuItems'][0]['content'][3]['text'] = f'Losses: {user.losses}'
    menu['menuItems'][0]['content'].append({
        'type': 'img',
        'src': f'{user.avatarDirect}',
        'identifier': 'avatarPic'
    })

    match_history = Games.objects.filter(players__player=user).order_by('-date_of_game')
    print(match_history)

    menu['menuItems'][1]['content'].append({
        'type': 'table',
        'class': 'w-100 d-flex flex-column justify-content-center align-items-center',
        'content': [
            {
                'type': 'thead',
                'class': 'thead-dark text-white w-100 d-flex flex-row justify-content-center gap-4',
                'content': [
                    {
                        'type': 'td',
                        'class': 'text-white',
                        'text': 'Date'
                    },
                    {
                        'type': 'td',
                        'class': 'text-white',
                        'text': 'Opponent'
                    },
                    {
                        'type': 'td',
                        'class': 'text-white',
                        'text': f'Winner'
                    }
                ]
            }
        ]
    })

    table = menu['menuItems'][1]['content'][0]['content']

    for match in match_history:
        opponent = (Players.objects.filter(game=match).exclude(player=user))[0]
        opponent_name = None

        if opponent.player is not None:
            opponent_name = opponent.player.username
            print(f"Opponent: {opponent.player.username}")
        else:
            opponent_name = opponent.guest_name
            print(f"Opponent: {opponent.guest_name}")

        table.append({
            'type': 'tr',
            'class': 'participant text-white',
            'content': [
                {
                    'type': 'td',
                    'class': 'text-white',
                    'text': f'{match.date_of_game}'
                },
                {
                    'type': 'td',
                    'class': 'text-white',
                    'text': opponent_name,
                },
                {
                    'type': 'td',
                    'class': 'text-white',
                    'text': f'{match.result}'
                }
            ]
        })

    return menu

def profile(request, menu_type='profile'):
    token = get_token_from_header(request)

    data = json.loads(request.body)
    user_of_profile = Users2.objects.get(username=data.get("user_of_profile"))
    print(f"USER_OF_PROFILE: {user_of_profile.wins}")
    user_of_query = Users2.objects.get(username=data.get("user_of_query"))
    try:
        friendship = Friends.objects.get(
            (Q(friend1=user_of_query) & Q(friend2=user_of_profile)) |
            (Q(friend1=user_of_profile) & Q(friend2=user_of_query)))
    except Friends.DoesNotExist:
        print("Friendship does not exist: views.py 1851\n")

    if (token == None) or (not validate_token(token)):
        menu = copy.deepcopy(MENU_DATA.get(menu_type))
    else:
        menu = modify_json_menu(menu_type, token)
        menu = fill_profile_with_user_data(menu, user_of_profile)
        if friendship.is_blocked:
            if friendship.blocker == user_of_query.username:
                menu['menuItems'][0]['content'].append({
                    'type': 'button',
                    'class': 'col-md-12 mt-2 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                    'identifier': user_of_profile.username,
                    'onclick': 'unblock(event)',
                    'text': 'UNBLOCK',
                },)
        else:
            menu['menuItems'][0]['content'].append({
                'type': 'button',
                'class': 'col-md-12 mt-2 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'identifier': user_of_profile.username,
                'onclick': 'block(event)',
                'text': 'BLOCK',
            },)
    if menu is not None:
        return JsonResponse(menu)
    else:
        return JsonResponse({'error': 'Menu type not found'}, status=404)

def open_chat(request):
    token = get_token_from_header(request)

    data = json.loads(request.body)
    target_friend_username = data.get('target_friend')
    source_friend_username = data.get('source_friend')

    try:
        target_friend = Users2.objects.get(username=target_friend_username)
        source_friend = Users2.objects.get(username=source_friend_username)
    except Users2.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    # Query the friendship between these two users
    try:
        friendship = Friends.objects.get(
            Q(friend1=target_friend, friend2=source_friend) |
            Q(friend1=source_friend, friend2=target_friend)
        )
    except Friends.DoesNotExist:
        return JsonResponse({'error': 'Friendship not found'}, status=404)

    if (token == None) or (not validate_token(token)):
        pass
    else:
        messages_queryset = Messages.objects.filter(friendship=friendship)

        # Populate the messages list
        messages_list = []
        for message in messages_queryset:
            messages_list.append({
                'sender': message.sender,
                'receiver': message.receiver,
                'message': message.message,
            })

        # Create the JsonResponse
        response = JsonResponse({
            'target_friend': target_friend.username,
            'source_friend': source_friend.username,
            'friendship_id': friendship.id,
            'is_blocked': friendship.is_blocked,
            'blocker': friendship.blocker,
            'messages': messages_list,
        })

        return response

    return JsonResponse({'error': 'Menu type not found'}, status=404)

def block_user(request):
    token = get_token_from_header(request)

    data = json.loads(request.body)
    if (token == None) or (not validate_token(token)):
        pass
    else:
        blocker_name = data.get('blocker')
        blocker = Users2.objects.get(username=blocker_name)
        blocked_name = data.get('blocked')
        blocked = Users2.objects.get(username=blocked_name)
        friendship = Friends.objects.get(
            (Q(friend1=blocker) & Q(friend2=blocked)) |
            (Q(friend1=blocked) & Q(friend2=blocker))
        )

        if not friendship.is_blocked:
            friendship.blocker = blocker_name
            friendship.is_blocked = True
            friendship.save()
    return JsonResponse({})


def unblock_user(request):
    token = get_token_from_header(request)

    data = json.loads(request.body)
    if (token == None) or (not validate_token(token)):
        pass
    else:
        unblocker_name = data.get('unblocker')
        unblocker = Users2.objects.get(username=unblocker_name)
        unblocked_name = data.get('unblocked')
        unblocked = Users2.objects.get(username=unblocked_name)
        friendship = Friends.objects.get(
            (Q(friend1=unblocker) & Q(friend2=unblocked)) |
            (Q(friend1=unblocked) & Q(friend2=unblocker))
        )

        if friendship.is_blocked:
            if friendship.blocker == unblocker_name:
                friendship.blocker = None
                friendship.is_blocked = False
                friendship.save()
    return JsonResponse({})