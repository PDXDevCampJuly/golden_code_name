from django.views.generic import ListView, UpdateView
from game.models import Board, Card, Clue
from .models import CardForm


class GameBoardList(ListView):
    """
    Implement Generic ListView
    """
    # limit our queryset to only the following columns
    model = Card
    template_name = 'spy.html'

    def get_context_data(self, **kwargs):
        """
        Implement our custom context data
        We are adding game_status data for context rendering.
        """
        context = super(GameBoardList, self).get_context_data(**kwargs)
        context['game_status'] = Board.objects.get()
        # TODO once we have working clue data
        context['clue'] = Clue.objects.all()
        return context


class UpdateCard(UpdateView):
    """
    Implement UpdateView
    """
    model = Card
    form_class = CardForm
    success_url = '/spy/'


