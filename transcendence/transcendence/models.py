from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

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
