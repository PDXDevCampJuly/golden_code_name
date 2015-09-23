from django.shortcuts import render
from django.views.generic import ListView
from game.models import Board, Card, Team

# Create your views here.

class GameBoardList(ListView):
    """
    Implement Generic ListView
    """
    model = Card
    template_name = 'spy.html'
    def get_context_data(self, **kwargs):
        """
        Implement our custom context data
        """
        context = super(GameBoardList, self).get_context_data(**kwargs)
        context['game_status']= Board.objects.get()
        return context





