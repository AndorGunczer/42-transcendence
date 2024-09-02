import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
# from transcendence.models import Users2 #returns error

class CommunicationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the WebSocket connection
        await self.accept()
        
        # Optionally, add user to a group for broadcast messages
        self.user = self.scope["user"]
        if self.user.is_authenticated:
            await self.channel_layer.group_add(
                f"user_{self.user.id}",
                self.channel_name
            )

    async def disconnect(self, close_code):
        # Optionally, remove user from group
        if self.user.is_authenticated:
            await self.channel_layer.group_discard(
                f"user_{self.user.id}",
                self.channel_name
            )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data.get('type')

        if message_type == 'chat_message':
            print("friend request is selected")
            await self.handle_chat_message(data)
        elif message_type == 'friend_request':
            await self.handle_friend_request(data)
        elif message_type == 'notification':
            await self.handle_notification(data)

    async def handle_chat_message(self, data):
        print("handle_chat_message is called")

    async def handle_friend_request(self, data):
        print("handle_friend_request is called")
        from transcendence.models import Users2

        sender_username = self.user.username  # Get the sender's username from the WebSocket connection
        receiver_username = data.get("receiver")

        try:
            # Try to get the receiver user object
            receiver = await sync_to_async(Users2.objects.get)(username=receiver_username)

            # Send a notification to the receiver's WebSocket group
            await self.channel_layer.group_send(
                f"user_{receiver.id}",
                {
                    'type': 'notification',
                    'message': f"You have a friend request from {sender_username}.",
                }
            )
        except Users2.DoesNotExist:
            # If the receiver does not exist, send a message back to the sender
            await self.send(text_data=json.dumps({
                'type': 'notification',
                'message': f"User {receiver_username} does not exist.",
            }))

        

        
        

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
            'message': event['message'],
        }))

    async def send_notification(self, event):
        await self.send(text_data=json.dumps({
            'type': 'notification',
            'message': event['message'],
        }))
