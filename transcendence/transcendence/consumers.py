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

from transcendence.models import Users2, Friends  # Adjust the import based on your project structure

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

        if message_type == 'chat_message':
            print("friend request is selected")
            await self.handle_chat_message(data)
        elif message_type == 'friend_request':
            await self.handle_friend_request(data)
        elif message_type == 'friend_acceptance':
            await self.handle_friend_acceptance(data)
        elif message_type == 'friend_declination':
            await self.handle_friend_declination(data)
        elif message_type == 'notification':
            await self.handle_notification(data)

    async def handle_chat_message(self, data):
        print("handle_chat_message is called")

    async def handle_friend_request(self, data):
        print("handle_friend_request is called")
        from transcendence.models import Users2

        sender_username = self.user.username
        receiver_username = data.get("receiver")

        try:
            receiver = await sync_to_async(Users2.objects.get)(username=receiver_username)
            # receiver = await sync_to_async(Users2.objects.get)(username=sender_username)
            try:
                await sync_to_async(Friends.objects.get)(
                    Q(state="pending") | Q(state="accepted"),
                    friend1=self.user,
                    friend2=receiver
                )
                print("Friendship has already been created")

                await self.channel_layer.group_send(
                    f"user_{self.user.id}",
                    {
                        'type': 'send_duplicate_friendship_notification',
                        'receiver': f"{receiver_username}",
                        'message': f"Friend request has already been sent {receiver_username}.",
                    }
                )
            except Friends.DoesNotExist:
                friendship = await sync_to_async(Friends)(friend1=self.user, friend2=receiver, state="pending")
                await sync_to_async(friendship.save)()

                try:
                    success_check = await sync_to_async(Friends.objects.get)(friend1=self.user, friend2=receiver, state="pending")
                    print(success_check)
                except Friends.DoesNotExist:
                    print(f'ERROR: Friends are not created in the database')

                # Debug print to verify group name and content of the message
                print(f"Sending friend request from {sender_username} to {receiver_username} in group user_{receiver.id}")
                
                await self.channel_layer.group_send(
                    f"user_{receiver.id}",
                    {
                        'type': 'send_friend_request',
                        'sender': f"{sender_username}",
                        'message': f"You have a friend request from {sender_username}.",
                    }
                )
                print("Message sent successfully")
            
        except Users2.DoesNotExist:
            await self.send(text_data=json.dumps({
                'type': 'notification',
                'message': f"User {receiver_username} does not exist.",
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
                    'message': f"Your friend request to {decliner} has been declined.",
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


        

        
        

    async def handle_notification(self, data):
        # Logic to handle incoming notification
        pass

    # Methods to send messages to client
    async def send_chat_message(self, event):
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': event['message'],
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
            'message': event['message'],
        }))
    
    async def send_duplicate_friendship_notification(self, event):
        await self.send(text_data=json.dumps({
            'type': 'friend_duplication_notification',
            'message': event['message'],
        }))