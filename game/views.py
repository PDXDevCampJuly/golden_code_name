from django.shortcuts import render
from random import  getrandbits, shuffle
from game.models import *

# Create your views here.


def clear_game():
    """Resets all data in the database to nothing"""
    Card.objects.all().delete()
    Team.objects.all().delete()
    Board.objects.all().delete()
    Clue.objects.all().delete()

def create_game_deck():
    """Creates the game"""
    # init deck
    deck = []

    #get starting team
    blueness = bool(getrandbits(1))
    if blueness == 1:
        BLUE = ['bl'] * 9
        RED = ['rd'] * 8
        BEIGE = ['bg'] *7
        deck.extend(BLUE)
        deck.extend(RED)
        deck.extend(BEIGE)
        deck.append('bk')
        team = Team(is_blue=True,spies_left = 9)
        team.save()
        team = Team(is_blue=False,spies_left = 8)
        team.save()
        #Sets the team that DOESN'T start, turn switching logic is allowed to switch it to the initial player.
    else:
        BLUE = ['bl'] * 8
        RED = ['rd'] * 9
        BEIGE = ['bg'] *7
        deck.extend(BLUE)
        deck.extend(RED)
        deck.extend(BEIGE)
        deck.append('bk')
        team = Team(is_blue=True,spies_left = 8)
        team.save()
        team = Team(is_blue=False,spies_left = 9)
        team.save()
    shuffle(deck)
    for card in deck:
        person = Card(word='foo',card_type=card)
        person.save()

def set_starting_board_conditions():
    starting_line = Board(is_blue = False, guesses_allowed = 0)
    starting_line.save()
    starting_line = Board(is_blue = True, guesses_allowed = 0)
    starting_line.save()

def start_game():
    clear_game()
    create_game_deck()
    set_starting_board_conditions()

def does_game_exist():
    if Card.objects.count() > 0:
        return True
    else:
        return False