#   This file is to give django information on database structure
#       and in more detail on how to build the database within postgresql.

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class Tournaments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, default="Not Set")
    creation_date = models.DateTimeField(auto_now=True)


class Avatar(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, default="Not Set")
    path = models.CharField(max_length=150, unique=True, default="Not Set")

class Games(models.Model):
    id = models.AutoField(primary_key=True)
    result = models.CharField(max_length=100, null=True, default="Not Set")
    date_of_game = models.DateTimeField(auto_now=True)
    tournament = models.ForeignKey(Tournaments, null=True, on_delete=models.CASCADE)

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
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=128, null=True)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    games = models.ForeignKey(Games, null=True, on_delete=models.CASCADE)
    # avatar = models.ForeignKey(Avatar, null=True, on_delete=models.SET_NULL)
    avatarDirect = models.CharField(max_length=200, null=True)
    allow_otp = models.BooleanField(default=False)

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
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Users2, null=True, on_delete=models.SET_NULL)
    guest_name = models.CharField(max_length=128, null=True)
    tournament = models.ForeignKey(Tournaments, null=True, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

class Players(models.Model):
    player = models.ForeignKey(Users2, null=True, on_delete=models.SET_NULL)
    game = models.ForeignKey(Games, null=True, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=128, null=True)