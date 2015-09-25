from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

# code_name Table

class Color(models.Model):
    """ This table holds the colors for the game """

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
    color = models.CharField(choices=CODE_NAME_CHOICES, max_length=2)


class Game(models.Model):
    """This table holds all the games on the site """
    current_turn = models.ForeignKey(Color)


class Team (models.Model):
    """ Table that holds all Teams """
    spies_left = models.PositiveSmallIntegerField(blank=True)
    color_id = models.ForeignKey(Color)
    game_id = models.ForeignKey(Game)


class Clue(models.Model):
    """ This table holds the clue and number from Spy Master """
    game_id = models.ForeignKey(Game)
    team_id = models.ForeignKey(Team)
    hint = models.CharField(max_length=50, default=None)
    number = models.PositiveSmallIntegerField(default=None)


class Word(models.Model):
    """ This table holds the words """
    word = models.CharField(max_length=50, primary_key=True)


class Card(models.Model):
    """This table holds the card content  """
    word_id = models.ForeignKey(Word)
    game_id = models.ForeignKey(Game)
    color_id = models.ForeignKey(Color)
    is_revealed = models.BooleanField(default=False)