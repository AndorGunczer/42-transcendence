# apps.py
from django.apps import AppConfig
from django.conf import settings
import os

class TranscendenceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transcendence'

    def ready(self):
        from transcendence.models import Avatar
        static_images_dir = os.path.join(settings.BASE_DIR, 'static', 'images')

        if os.path.exists(static_images_dir):
            image_files = os.listdir(static_images_dir)
            for image_file in image_files:
                if not Avatar.objects.filter(name=image_file).exists():
                    Avatar.objects.create(
                        name=image_file,
                        path=os.path.join('static/images', image_file)
                    )
