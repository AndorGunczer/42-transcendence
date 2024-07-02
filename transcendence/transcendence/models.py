from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class Tournaments(models.Model):
    name = models.CharField(max_length=100, unique=True, default="Not Set")
    creation_date = models.DateTimeField()


class Avatar(models.Model):
    name = models.CharField(max_length=100, unique=True, default="Not Set")
    path = models.CharField(max_length=150, unique=True, default="Not Set")

class Games(models.Model):
    player1 = models.CharField(max_length=20)
    player2 = models.CharField(max_length=20)
    result = models.BooleanField()
    date_of_game = models.DateTimeField()

    def __str__(self):
        return str(self.date_of_game)

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class Users2(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    games = models.ForeignKey(Games, null=True, on_delete=models.SET_NULL)
    avatar = models.ForeignKey(Avatar, null=True, on_delete=models.SET_NULL)
    avatarDirect = models.CharField(max_length=200, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def increment_wins(self):
        self.wins += 1

    def decrement_wins(self):
        self.losses += 1

    def has_perm(self, perm, obj=None):
        # Handle custom permissions if needed
        return True

    def has_module_perms(self, app_label):
        # Handle custom permissions if needed
        return True

    @property
    def is_staff(self):
        return self.is_superuser

class Participants(models.Model):
    player_id = models.ForeignKey(Users2, null=True, on_delete=models.SET_NULL)
    tournament_id = models.ForeignKey(Tournaments, null=True, on_delete=models.SET_NULL)

class Tournament_Games(models.Model):
    game_id = models.IntegerField(primary_key=True)
    player1_id = models.ForeignKey(Users2, null=True, on_delete=models.SET_NULL, related_name='tournament_games_player1')
    player2_id = models.ForeignKey(Users2, null=True, on_delete=models.SET_NULL, related_name='tournament_games_player2')
    tournament_id = models.ForeignKey(Tournaments, null=True, on_delete=models.SET_NULL)