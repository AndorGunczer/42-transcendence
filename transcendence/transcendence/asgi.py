"""
ASGI config for transcendence project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chat.consumers import ChatConsumer  #later replacing with a child class
from django.core.management import call_command
from asgiref.sync import sync_to_async

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transcendence.settings')

# Setup Django before importing models or running commands
django.setup()


application = ProtocolTypeRouter({
	'https': get_asgi_application(),
	'http': get_asgi_application(),
	'websocket': URLRouter([
        path('chat/<str:receiver>', ChatConsumer.as_asgi()),
		path('chat', ChatConsumer.as_asgi()),
    ])
})

# Run the populate_avatars command

try:
	call_command('populate_avatars')
except Exception as e:
	print(f"Error populating avatars: {e}")


# async def populate():
# 	try:
# 		await sync_to_async(call_command)('populate_avatars')
# 	except Exception as e:
# 		print(f"Error populating avatars: {e}")

# populate()

