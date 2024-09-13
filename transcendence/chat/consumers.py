from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import json

# class ChatConsumer(WebsocketConsumer):
# 	def receive(self, text_data):
# 		# print(f"receive started")
# 		data_dict = json.loads(text_data)
# 		message = data_dict["message"] #we extract text message
# 		# print(f"msg received {message}")
# 		msg_json = json.dumps({"message" : message})#convert to json format
# 		self.send(msg_json)#sending message back to client
# 		#to do: send a message to a certain client

# 	def connect(self):
# 		self.accept()
# 		print(f"c accepted")

class ChatConsumer(AsyncWebsocketConsumer):
	async def receive(self, text_data):
		# print(f"receive started")
		data_dict = json.loads(text_data)
		message = data_dict["message"] #we extract text message
		receiver = data_dict["receiver"]
		sender = data_dict["sender"]
		# print(f"msg received {message}")
		msg_json = json.dumps({"message" : message, "sender" : sender, "receiver" : receiver})#convert to json format
		print(f"c receiver {receiver}")
		print(f"c sender {sender}")
		await self.send(msg_json)#sending message back to client
		#to do: send a message to a certain client

	async def connect(self):
		await self.accept()
		print(f"c accepted")