from django.shortcuts import render
from random import  getrandbits, shuffle

# Create your views here.

def create_game_deck():
    # init deck
    deck = []

    #get starting team
    is_blue = bool(getrandbits(1))
    if is_blue == 1:
        BLUE = ['bl'] * 9
        RED = ['rd'] * 8
        BEIGE = ['bg'] *7
        deck.extend(BLUE)
        deck.extend(RED)
        deck.extend(BEIGE)
        deck.append('bk')
    else:
        BLUE = ['bl'] * 8
        RED = ['rd'] * 9
        BEIGE = ['bg'] *7
        deck.extend(BLUE)
        deck.extend(RED)
        deck.extend(BEIGE)
        deck.append('bk')
    shuffle(deck)
    return (is_blue,deck)
