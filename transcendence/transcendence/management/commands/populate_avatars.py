# your_app/management/commands/populate_avatars.py
from django.core.management.base import BaseCommand
from your_app.models import Avatar
import os

class Command(BaseCommand):
    help = 'Populate the Avatar table with initial data'

    def handle(self, *args, **kwargs):
        static_images_dir = os.path.join(os.path.dirname(__file__), '../../static/images')
        if not os.path.exists(static_images_dir):
            self.stdout.write(self.style.ERROR('Static images directory does not exist'))
            return

        image_files = os.listdir(static_images_dir)
        for image_file in image_files:
            if not Avatar.objects.filter(name=image_file).exists():
                Avatar.objects.create(
                    name=image_file,
                    path=os.path.join('static/images', image_file)
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated Avatar table'))
