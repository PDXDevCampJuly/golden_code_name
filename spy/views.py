from django.shortcuts import render
from django.views.generic import ListView
from game.models import Board, Card, Clue

# Create your views here.

class GameBoardList(ListView):
    """
    Implement Generic ListView
    """
    queryset = Card.objects.all().only('word', 'id', 'selected')
    template_name = 'spy.html'
    def get_context_data(self, **kwargs):
        """
        Implement our custom context data
        """
        context = super(GameBoardList, self).get_context_data(**kwargs)
        context['game_status'] = Board.objects.get()
        # TODO once we have working clue data
        # context['clue'] = Clue.objects.get().last()
        return context





