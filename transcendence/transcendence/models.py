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
    password = models.CharField(max_length=20)
    score = models.IntegerField()
    games = models.ForeignKey(Games, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.username
    
    def make_password(self, password):
        self.password = make_password(password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)