"""
ASGI config for transcendence project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transcendence.settings')

# Setup Django before importing models or running commands
django.setup()

application = get_asgi_application()

# Run the populate_avatars command
try:
    call_command('populate_avatars')
except Exception as e:
    print(f"Error populating avatars: {e}")

