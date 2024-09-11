# apps.py
from django.apps import AppConfig
from django.conf import settings
import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver

# Configuration of application (upon startup)

class TranscendenceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transcendence'

    def ready(self):
        post_migrate.connect(populate_avatar_table, sender=self)

@receiver(post_migrate)
def populate_avatar_table(sender, **kwargs):
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
