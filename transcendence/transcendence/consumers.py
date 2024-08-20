import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Perform actions when a WebSocket connection is established
        await self.accept()

    async def disconnect(self, close_code):
        # Perform actions when a WebSocket connection is closed
        pass

    async def receive(self, text_data):
        # Handle receiving data through WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send a message back through WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))


class FriendRequestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Perform actions when a WebSocket connection is established
        await self.accept()

    async def disconnect(self, close_code):
        # Perform actions when a WebSocket connection is closed
        pass

    async def receive(self, text_data):
        # Handle receiving data through WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send a message back through WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
