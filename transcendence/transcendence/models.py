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
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    score = models.IntegerField()
    games = models.ForeignKey(Games, on_delete=models.CASCADE)

    def __str__(self):
        return self.username