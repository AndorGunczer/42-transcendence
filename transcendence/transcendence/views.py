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
from transcendence.web3_utils import add_tournament, add_participant, increment_score, set_winner, get_tournament_count, get_tournament, get_participant_score, get_participant_list, get_tournament_index_by_name  
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
        username = list(participants.keys())[0]
        user = None
        participant = None
        tournament = None
        try:
            # First, try to retrieve the Users2 object
            user = Users2.objects.get(username=username)
            
            # Retrieve the Participants object based on the user
            participant = Participants.objects.get(player=user)
            
        except Users2.DoesNotExist:
            # If the user does not exist, look for a participant with the guest name
            participant = Participants.objects.filter(guest_name=username).first()
        
        if participant is not None:
            # Get the tournament associated with the participant
            tournament = participant.tournament


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

    # Users2.objects.get(username=player1)
    # create game database instance and 2 player instances joined into game
    game_db = Games()
    game_db.save()

    try:
        player1_db = Players(player=Users2.objects.get(username=player1), game=game_db)
    except Users2.DoesNotExist:
        player1_db = Players(game=game_db, guest_name=player1)
    player1_db.save()
    try:
        player2_db = Players(player=Users2.objects.get(username=player2), game=game_db)
    except Users2.DoesNotExist:
        player2_db = Players(game=game_db, guest_name=player2)
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

    # Create Tournament in the Database
    tournament_db = Tournaments(name=tournament_name)
    tournament_db.save()

    # Create Tournament on the Blockchain
    receipt = add_tournament(tournament_name, "No Winner Yet")
    print(f"addTournament transaction successful with hash: {receipt.transactionHash.hex()}")

    for participant in participants:
        if participant == None: continue
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
        # REWORK WITH BLOCKCHAIN

        # Database Implementation
        participants = Participants.objects.filter(tournament__name=tournament_name).order_by('-points')
        print(participants)

        # Blockchain Implementation
        participants_b = {}
        index = get_tournament_index_by_name(tournament_name)
        p_list = get_participant_list(index)

        for participant in p_list:
            print("ROUND")
            participants_b[participant] = get_participant_score(index, participant)

        # Sort Dictionary in Reverse order based on Values

        participants_b = {key: val for key, val in sorted(participants_b.items(), key = lambda ele: ele[1], reverse = True)}

        print(participants_b)

        menu = modify_json_menu(menu_type, token)
        response_data = tournament_select_page_fill(menu, participants_b)

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

    response_data = {'menu': menu, 'game_id': data['game_id'], 'player1': player1, 'player1_id': players[0].id, 'player2': players2, 'player2_id': players[1].id}

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

        # blockchain
        print(game_db.tournament.name)
        # blockchain_tournament = get_tournament_index_by_name(game_db.tournament.name)
        # print(blockchain_tournament)

        # blockchain end

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

                # Update Participants.points for the winner in Database
                participant = Participants.objects.get(player=player1_db, tournament=game.tournament)
                participant.points += 1
                participant.save()

                # Update Participants.points for the winner on the Blockchain
                receipt = increment_score(get_tournament_index_by_name(game_db.tournament.name), participant.player.username, 1)
                print(f"incrementScore transaction successful with hash: {receipt.transactionHash.hex()}")
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

                # Update Participants.points for the winner in Database
                participant = Participants.objects.get(player=player2_db, tournament=game.tournament)
                participant.points += 1
                participant.save()

                # Update Participants.points for the winner on the Blockchain
                receipt = increment_score(get_tournament_index_by_name(game_db.tournament.name), participant.player.username, 1)
                print(f"incrementScore transaction successful with hash: {receipt.transactionHash.hex()}")
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
            # Set Tournament Winner on the Blockchain
            set_winner(get_tournament_index_by_name(game_db.tournament.name), tournament_winner.player.username)

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
import smtplib, ssl
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

                    with open('output.txt', 'w') as file:
                        file.write("2fa is active\n")

                        try:
                            # Configuration
                            port = 465
                            smtp_server = "smtp.gmail.com"
                            sender_email = "ft.transcendence.2fa.42@gmail.com"
                            receiver_email = user.email
                            email_password = 'rwsv qnsl lqfa shic'
                            message = f"""\
                            Subject: Your OTP Code

                            Your OTP code is {otp}."""
                            context = ssl.create_default_context()

                            file.write("Preparing to connect to the SMTP server\n")
                            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                                file.write("Connection to server was successful\n")
                                server.login(sender_email, email_password)
                                file.write("Login to the SMTP server was successful\n")
                                server.sendmail(sender_email, receiver_email, message)
                                file.write("Email sent successfully\n")

                        except smtplib.SMTPException as e:
                            file.write(f"SMTP error occurred: {e}\n")
                            return JsonResponse({'error': 'Failed to send email'}, status=500)
                        except Exception as e:
                            file.write(f"An error occurred: {e}\n")
                            return JsonResponse({'error': 'An unexpected error occurred'}, status=500)

                    return JsonResponse({'status': 'otp_sent'})
                else:
                    login(request, user)
                    access_token = str(AccessToken.for_user(user))

                    # Assuming modify_json_menu requires a token and modifies the menu accordingly
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