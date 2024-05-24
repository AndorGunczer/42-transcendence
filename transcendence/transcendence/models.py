from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils import timezone
import datetime

class Games(models.Model):
    player1 = models.CharField(max_length=20)
    player2 = models.CharField(max_length=20)
    result = models.BooleanField()
    date_of_game = models.DateTimeField()

    def __str__(self):
        return self.date_of_game

class Users(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    wins = models.IntegerField()
    losses = models.IntegerField()
    games = models.ForeignKey(Games, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def increment_wins(self):
        self.wins += 1

    def decrement_wins(self):
        self.losses += 1
