# your_app/management/commands/populate_avatars.py
from django.core.management.base import BaseCommand
from transcendence.models import Users2, Avatar, Friends
from django.db.models import Q
import os

class Command(BaseCommand):
    help = 'Populate the Avatar table with initial data'

    def handle(self, *args, **kwargs):
        static_images_dir = os.path.join(os.path.dirname(__file__), '../../../static/images')
        if not os.path.exists(static_images_dir):
            self.stdout.write(self.style.ERROR('Static images directory does not exist'))
            return

        # Create users with hashed passwords
        users = [
            {"username": "test1", "password": "12345", "email": "andor.gunczer@gmail.com", "avatarDirect": "https://localhost/static/images/anolis_avatar.jpg", "twofa": "True"},
            {"username": "test2", "password": "12345", "email": "andor.gunczer@gmail.com", "avatarDirect": "https://localhost/static/images/cat_avatar.jpg", "twofa": "False"},
            {"username": "test3", "password": "12345", "email": "andor.gunczer@gmail.com", "avatarDirect": "https://localhost/static/images/dog_avatar.jpg", "twofa": "False"},
            {"username": "test4", "password": "12345", "email": "andor.gunczer@gmail.com", "avatarDirect": "https://localhost/static/images/birb.jpeg", "twofa": "true"},
        ]

        users_db = []

        for user_data in users:
            user, created = Users2.objects.get_or_create(username=user_data["username"])
            if created:
                user.set_password(user_data["password"])
                user.email = user_data["email"]
                user.avatarDirect = user_data["avatarDirect"]
                user.twofa = user_data["twofa"]
                user.save()
                users_db.append(user)
            else:
                self.stdout.write(self.style.WARNING(f'User {user_data["username"]} already exists'))

        for user in users_db:
            if user.username == "test4": continue
            other_users = Users2.objects.all().exclude(Q(username=user.username) | Q(username="test4"))

            for other_user in other_users:
                try: 
                    friendship = Friends.objects.get(
                        Q(friend1=other_user, friend2=user) |
                        Q(friend1=user, friend2=other_user)
                    )

                except Friends.DoesNotExist:
                    new_friendship = Friends(friend1=user, friend2=other_user, state="accepted")
                    new_friendship.save()



        # Populate Avatar table
        image_files = os.listdir(static_images_dir)
        for image_file in image_files:
            if not Avatar.objects.filter(name=image_file).exists():
                Avatar.objects.create(
                    name=image_file,
                    path=os.path.join('static/images', image_file)
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated Avatar table'))

