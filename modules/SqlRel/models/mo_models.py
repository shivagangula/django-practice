from django.db import models


class Game(models.Model):
    game_name = models.CharField(max_length=10)
    game_company = models.CharField(max_length=10)
    game_rating = models.FloatField()


class Player(models.Model):
    name = models.CharField(max_length=10)



