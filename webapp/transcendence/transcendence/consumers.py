import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
# from transcendence.models import Users2 #returns error
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken
from django.conf import settings
import jwt
from django.db.models import Q

from transcendence.models import Users2, Friends, Messages  # Adjust the import based on your project structure

class CommunicationConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # Retrieve token from cookies
        token = self.scope['cookies'].get('access_token', None)

        # If token is not in cookies, check query parameters (fallback)
        if not token:
            query_string = self.scope['query_string'].decode('utf-8')
            params = dict(param.split('=') for param in query_string.split('&') if '=' in param)
            token = params.get('access_token', None)

        self.user = await self.get_user_from_token(token)

        # Debug: Print user information
        print(f"User in connect: {self.user} (Authenticated: {self.user.is_authenticated})")

        if self.user.is_authenticated:
            await self.channel_layer.group_add(
                f"user_{self.user.id}",
                self.channel_name
            )

            # Add the user to the 'online_users' group
            await self.channel_layer.group_add(
                "online_users",  # Group name
                self.channel_name  # Channel name for this user connection
            )

            await self.set_user_online(self.user)
            await self.accept()
        else:
            await self.close()

    @sync_to_async
    def get_user_from_token(self, token):
        token = AccessToken(token)
        user_id = token.payload['user_id']
        user = Users2.objects.get(id=user_id)

        return user

    async def disconnect(self, close_code):
        if self.user.is_authenticated:
            await self.channel_layer.group_discard(
                f"user_{self.user.id}",
                self.channel_name
            )

            await self.set_user_offline(self.user)

            await self.channel_layer.group_discard(
                "online_users",  # Group name
                self.channel_name  # Channel name for this user connection
            )

    async def set_user_online(self, user):
        user.is_online = True
        await database_sync_to_async(user.save)()

        # Notify other connected users
        await self.channel_layer.group_send(
            "online_users",  # A group for tracking online users
            {
                "type": "send_user_to_online",
                "user_id": user.id,
                "user_name": user.username,
            }
        )

    async def set_user_offline(self, user):
        user.is_online = False
        #edit scores if updated in the database
        user_db = await sync_to_async(Users2.objects.get)(username=user.username)
        if (user_db.wins > user.wins or user_db.losses > user.losses):
            user.wins = user_db.wins
            user.losses = user_db.losses
        await database_sync_to_async(user.save)()

        # Notify other connected users
        await self.channel_layer.group_send(
            "online_users",  # A group for tracking online users
            {
                "type": "send_user_to_offline",
                "user_id": user.id,
                "user_name": user.username,
            }
        )

    # @database_sync_to_async
    # def get_user(self):
    #     user = self.scope.get("user", None)
    #     if user is not None:
    #         print(f"User in scope: {user}, Authenticated: {user.is_authenticated}")
    #         if user.is_authenticated:
    #             return user
    #     return AnonymousUser()

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data.get('type')
        user = await sync_to_async(Users2.objects.get)(id=self.user.id)
        self.user = user

        if message_type == 'update':
            pass
        elif message_type == 'apply_match_invitation':
            print("apply_match_invitation")
            await self.handle_apply_match_invitation(data)
        elif message_type == 'decline_match_invitation':
            print("decline_match_invitation")
            await self.handle_decline_match_invitation(data)
        elif message_type == 'chat_invite':
            await self.handle_chat_invite(data)
        elif message_type == 'chat_message':
            print("friend request is selected")
            await self.handle_chat_message(data)
        # elif message_type == 'user_online':
        #     await self.handle_user
        elif message_type == 'friend_request':
            await self.handle_friend_request(data)
        elif message_type == 'friend_acceptance':
            await self.handle_friend_acceptance(data)
        elif message_type == 'friend_declination':
            await self.handle_friend_declination(data)
        elif message_type == 'settings_save':
            await self.handle_settings_save(data)
        elif message_type == 'notification':
            await self.handle_notification(data)
 # async def send_apply_match_invitation(self, event):
    #     await self.send(text_data=json.dumps({
    #         'type': 'apply_match_invitation',
    #         'sender': event['sender'],
    #         'receiver': event['receiver'],
    #         'friendship_id': event['friendship_id'],
    #         'message': event['message'],
    #     }))

    # async def send_decline_match_invitation(self, event):
    #     await self.send(text_data=json.dumps({
    #         'type': 'decline_match_invitation',
    #         'sender': event['sender'],
    #         'receiver': event['receiver'],
    #         'friendship_id': event['friendship_id'],
    #         'message': event['message'],
    #     }))

    async def handle_decline_match_invitation(self, data):
        print("--------------handle_decline_match_invitation---------------")
        sender = await sync_to_async(Users2.objects.get)(username=data.get("sender"))
        receiver = await sync_to_async(Users2.objects.get)(username=data.get("receiver"))
        friendship_id = data.get("friendship_id")
        friendship = await sync_to_async(Friends.objects.get)(id=friendship_id)

        await self.channel_layer.group_send(
                f"user_{receiver.id}",
                {
                    'type': 'send_decline_match_invitation',
                    'sender': sender.username,
                    'receiver': receiver.username,
                    'friendship_id': friendship_id,
                }
            )


    async def handle_apply_match_invitation(self, data):
        print("--------------handle_apply_match_invitation---------------")
        sender = await sync_to_async(Users2.objects.get)(username=data.get("sender"))
        receiver = await sync_to_async(Users2.objects.get)(username=data.get("receiver"))
        friendship_id = data.get("friendship_id")
        friendship = await sync_to_async(Friends.objects.get)(id=friendship_id)

        await self.channel_layer.group_send(
                f"user_{receiver.id}",
                {
                    'type': 'send_apply_match_invitation',
                    'sender': sender.username,
                    'receiver': receiver.username,
                    'friendship_id': friendship_id,
                }
            )

    async def handle_chat_invite(self, data):
        print("handle_chat_invite is called")
        sender = await sync_to_async(Users2.objects.get)(username=data.get("sender"))
        receiver = await sync_to_async(Users2.objects.get)(username=data.get("receiver"))
        friendship_id = data.get("friendship_id")
        friendship = await sync_to_async(Friends.objects.get)(id=friendship_id)
        message = data.get("message")

        new_message = await sync_to_async(Messages)(friendship=friendship, sender=sender.username, receiver=receiver.username, message=message)
        await sync_to_async(new_message.save)()

        await self.channel_layer.group_send(
                f"user_{sender.id}",
                {
                    'type': 'send_chat_invite',
                    'sender': sender.username,
                    'receiver': receiver.username,
                    'friendship_id': friendship_id,
                    'message': message,
                }
            )

        await self.channel_layer.group_send(
                f"user_{receiver.id}",
                {
                    'type': 'send_chat_invite',
                    'sender': sender.username,
                    'receiver': receiver.username,
                    'friendship_id': friendship_id,
                    'message': message,
                }
            )

    async def handle_chat_message(self, data):
        from .serializers import MessageSerializer
        print("handle_chat_message is called")

        sender = await sync_to_async(Users2.objects.get)(username=data.get("sender"))
        receiver = await sync_to_async(Users2.objects.get)(username=data.get("receiver"))
        friendship_id = data.get("friendship_id")
        friendship = await sync_to_async(Friends.objects.get)(id=friendship_id)
        message_text = data.get("message")

        if friendship.is_blocked:
            return None

        # Prepare the message data to be serialized
        message_data = {
            'friendship_id': f'{friendship.id}',
            'sender': sender.username,
            'receiver': receiver.username,
            'message': message_text
        }

        # Serialize the data
        serializer = MessageSerializer(data=message_data)

        if serializer.is_valid():
            # Save the serialized data asynchronously
            await sync_to_async(serializer.save)()
        else:
            print(serializer.errors)
            return None

        # Send the message to the sender and receiver groups
        await self.channel_layer.group_send(
            f"user_{sender.id}",
            {
                'type': 'send_chat_message',
                'sender': sender.username,
                'receiver': receiver.username,
                'friendship_id': friendship_id,
                'message': message_text,
            }
        )

        await self.channel_layer.group_send(
            f"user_{receiver.id}",
            {
                'type': 'send_chat_message',
                'sender': sender.username,
                'receiver': receiver.username,
                'friendship_id': friendship_id,
                'message': message_text,
            }
        )






    async def handle_friend_request(self, data):
        from transcendence.models import Users2, Friends
        from transcendence.serializers import FriendRequestSerializer

        sender_username = self.user.username
        serializer = FriendRequestSerializer(data=data)

        if serializer.is_valid():
            receiver_username = serializer.validated_data.get("receiver")
            if receiver_username == sender_username:
                f"user_{self.user.id}",
                {
                    'type': 'send_notification',
                    'message': f"YoU sErIoUs BoII?!.",
                }
            else:
                try:
                    receiver = await sync_to_async(Users2.objects.get)(username=receiver_username)

                    try:
                        await sync_to_async(Friends.objects.get)(
                            Q(state="pending") | Q(state="accepted"),
                            friend1=self.user,
                            friend2=receiver
                        )
                        await self.channel_layer.group_send(
                            f"user_{self.user.id}",
                            {
                                'type': 'send_duplicate_friendship_notification',
                                'receiver': f"{receiver_username}",
                                'message': f"Friend request has already been sent to {receiver_username}.",
                            }
                        )
                    except Friends.DoesNotExist:
                        friendship = await sync_to_async(Friends)(friend1=self.user, friend2=receiver, state="pending")
                        await sync_to_async(friendship.save)()

                        await self.channel_layer.group_send(
                            f"user_{receiver.id}",
                            {
                                'type': 'send_friend_request',
                                'sender': f"{sender_username}",
                                'message': f"You have a friend request from {sender_username}.",
                            }
                        )
                except Users2.DoesNotExist:
                    await self.send(text_data=json.dumps({
                        'type': 'notification',
                        'message': f"User {receiver_username} does not exist.",
                    }))
        else:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Invalid data received',
                'errors': serializer.errors,
            }))


    async def handle_friend_acceptance(self, data):
        acceptor = await sync_to_async(Users2.objects.get)(username=data.get('acceptor'))
        accepted = await sync_to_async(Users2.objects.get)(username=data.get('accepted'))

        friendship = await sync_to_async(Friends.objects.get)(friend1=accepted, friend2=acceptor, state="pending")
        friendship.state = "accepted"
        await sync_to_async(friendship.save)()

        await self.channel_layer.group_send(
                f"user_{accepted.id}",
                {
                    'type': 'send_friend_acceptance_notification',
                    'acceptor': acceptor.username,
                    'accepted': accepted.username,
                    'message': f"Your friend request to {acceptor.username} has been accepted.",
                }
            )

        await self.channel_layer.group_send(
            f"user_{acceptor.id}",
            {
                'type': 'send_friend_acceptance_notification',
                'acceptor': acceptor.username,
                'accepted': accepted.username,
                'message': f"Your friend request to {acceptor.username} has been accepted.",
            }
        )

    async def handle_friend_declination(self, data):
        decliner = await sync_to_async(Users2.objects.get)(username=data.get('decliner'))
        declined = await sync_to_async(Users2.objects.get)(username=data.get('declined'))

        friendship = await sync_to_async(Friends.objects.get)(friend1=declined, friend2=decliner, state="pending")
        friendship.state = "declined"
        await sync_to_async(friendship.delete)()

        await self.channel_layer.group_send(
                f"user_{declined.id}",
                {
                    'type': 'send_friend_declination_notification',
                    'decliner': decliner.username,
                    'declined': declined.username,
                    'message': f"Your friend request to {decliner} has been declined.",
                }
            )

        await self.channel_layer.group_send(
                f"user_{decliner.id}",
                {
                    'type': 'send_friend_declination_notification',
                    'decliner': decliner.username,
                    'declined': declined.username,
                    'message': f"You declined the friend request to {decliner}.",
                }
            )

    async def handle_duplicate_friendship(self, data):
        decliner = data.get('decliner')
        declined = await sync_to_async(Users2.objects.get)(username=data.get('declined'))

        await self.channel_layer.group_send(
                f"user_{declined.id}",
                {
                    'type': 'send_friend_declination_notification',
                    'message': f"Your friend request to {decliner} has been declined.",
                }
            )

    async def handle_settings_save(self, data):
        # Fetch the updated user data from the database when an event happens
        new_user = await sync_to_async(Users2.objects.get)(id=self.user.id)
        print(f'SOCKET ID: {self.user.id}\nSOCKET USERNAME: {self.user.username}')
        print("handle_settings_save is CALLED")
        # username = data.get('new_username')
        # avatarDirect = data.get('new_avatarDirect')
        # print(f'{username}, {avatarDirect}')

        # Update WebSocket state with the new data
        # self.scope["user"].username = username
        # self.scope["user"].avatarDirect = avatarDirect
        # self.user.username = username
        # self.user.avatarDirect = f'https://localhost/static/images/{avatarDirect}'
        self.user = new_user
        await sync_to_async(self.user.save)()
        print(f'SOCKET ID: {self.user.id}\nSOCKET USERNAME: {self.user.username}')
        print("SCOPE IS UPDATED")
        # print(f'{self.scope["user"].username}, {self.scope["user"].avatarDirect}')
        # print(f'username {self.user.username}')






    async def handle_notification(self, data):
        # Logic to handle incoming notification
        pass

    # Methods to apply or decline match invitation

    async def send_apply_match_invitation(self, event):
        await self.send(text_data=json.dumps({
            'type': 'apply_match_invitation',
            'sender': event['sender'],
            'receiver': event['receiver'],
            'friendship_id': event['friendship_id'],
        }))

    async def send_decline_match_invitation(self, event):
        await self.send(text_data=json.dumps({
            'type': 'decline_match_invitation',
            'sender': event['sender'],
            'receiver': event['receiver'],
            'friendship_id': event['friendship_id'],
        }))

    # Methods to send messages to client
    async def send_chat_message(self, event):
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'sender': event['sender'],
            'receiver': event['receiver'],
            'friendship_id': event['friendship_id'],
            'message': event['message'],
        }))

    async def send_chat_invite(self, event):
        await self.send(text_data=json.dumps({
            'type': 'chat_invite',
            'sender': event['sender'],
            'receiver': event['receiver'],
            'friendship_id': event['friendship_id'],
            'message': event['message'],
        }))


    async def send_user_to_online(self, event):
        await self.send(text_data=json.dumps({
            'type': 'set_user_to_online',
            'target_user_id': event['user_id'],
            'target_user_name': event['user_name'],
        }))

    async def send_user_to_offline(self, event):
        await self.send(text_data=json.dumps({
            'type': 'set_user_to_offline',
            'target_user_id': event['user_id'],
            'target_user_name': event['user_name'],
        }))

    async def send_friend_request(self, event):
        await self.send(text_data=json.dumps({
            'type': 'friend_request',
            'sender': event['sender'],
            'message': event['message'],
        }))

    async def send_notification(self, event):
        await self.send(text_data=json.dumps({
            'type': 'notification',
            'message': event['message'],
        }))

    async def send_friend_acceptance_notification(self, event):
        await self.send(text_data=json.dumps({
            'type': 'friend_acceptance_notification',
            'acceptor': event['acceptor'],
            'accepted': event['accepted'],
            'message': event['message'],
        }))

    async def send_friend_declination_notification(self, event):
        await self.send(text_data=json.dumps({
            'type': 'friend_declination_notification',
            'decliner': event['decliner'],
            'declined': event['declined'],
            'message': event['message'],
        }))

    async def send_duplicate_friendship_notification(self, event):
        await self.send(text_data=json.dumps({
            'type': 'friend_duplication_notification',
            'message': event['message'],
        }))

    async def tournament_broadcast(self, event):
        await self.send(text_data=json.dumps({
            'type': 'tournament_broadcast',
            'message': event['message']
        }))
