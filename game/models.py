from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

# code_name Table

class Team (models.Model):
    is_blue = models.BooleanField(primary_key = True)
    spies_left = models.PositiveSmallIntegerField()

class Board(models.Model):
    is_blue = models.BooleanField(primary_key = True)
    guesses_allowed = models.PositiveSmallIntegerField()

class Clue(models.Model):
    clue = models.CharField(max_length = 50)
    num_of_cards = models.PositiveSmallIntegerField()
    team = models.ForeignKey(Team)

class Card(models.Model):
    word = models.CharField(max_length = 50)
    selected = models.BooleanField(default = False)
    BLUE = 'bl'
    RED = 'rd'
    BEIGE = 'bg'
    BLACK = 'bk'
    CODE_NAME_CHOICES = (
        (BLUE, 'Blue Team'),
        (RED, 'Red Team'),
        (BEIGE, 'Bystander'),
        (BLACK, 'Assassin'),
    )
    card_type = models.CharField(max_length=2, choices=CODE_NAME_CHOICES)