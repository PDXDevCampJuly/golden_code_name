from django.shortcuts import render, redirect
from random import choice, shuffle
from game.models import *
from django.contrib.contenttypes.models import ContentType

# Create your views here.



def new_game():
    # wanting to initialize red and blue turns 50% of the time
    possible_starting_colors = [Color.objects.get(color='bl'), Color.objects.get(color='rd')]
    starting_color = choice(possible_starting_colors)
    current_game = Game(current_turn=starting_color)
    current_game.save()

    possible_starting_colors.pop(possible_starting_colors.index(starting_color))

    new_team = Team(game_id=current_game, color_id=starting_color, spies_left=9)
    new_team.save()
    new_team_two = Team(game_id=current_game, color_id=possible_starting_colors[0],
                        spies_left=8)
    new_team_two.save()

    list_of_words = []
    for word in Word.objects.order_by('?')[:25]:
        list_of_words.append(word)

    Card(color_id=Color.objects.get(color='bk'), word_id=list_of_words.pop(),
         game_id=current_game).save()

    beige = Color.objects.get(color='bg')
    for bystander in range(7):
        Card(color_id=beige,
             word_id=list_of_words.pop(),
             game_id=current_game).save()

    for starting_team in range(9):
        Card(color_id=starting_color,
             word_id=list_of_words.pop(),
             game_id=current_game).save()



    for starting_team in range(8):
        Card(color_id=possible_starting_colors[0],
             word_id=list_of_words.pop(),
             game_id=current_game).save()


def start_index_page(request):
    if request.method == 'POST':
        new_game()
        return redirect('/select/')
    else:
        return render(request, 'index.html')


def select_player(request):
    return render(request, 'select_player.html')
