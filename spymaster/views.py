from django.shortcuts import render
from game.models import *

# Create your views here.

def spymaster_page(request):
    game_board = Card.objects.all()
    turn = Board.objects.first()
    blue_team = Team.objects.get(is_blue=True)
    red_team = Team.objects.get(is_blue=False)
    if request.method == 'POST':
        clues = request.POST
        newclue = Clue(clue=clues['clue'],num_of_cards=clues['moves'],team = turn.active_team)
        #fix when turn change logic exists
        turns = Board(is_blue = turn.active_team.is_blue, num_of_cards =clues['moves'], active_team = turn.active_team)
        #Board.objects.first() = turns
        newclue.save()
    return render(request, 'spymaster_hooks.html',{'game_board':game_board,'turn':turn,'blue_team':blue_team,'red_team':red_team})
