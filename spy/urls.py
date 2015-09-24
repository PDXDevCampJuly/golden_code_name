from django.conf.urls import url
from .views import GameBoardList, UpdateCard

urlpatterns = [
    url(r'^$', GameBoardList.as_view()),
    url(r'^(?P<pk>\d+)/$', UpdateCard.as_view()),
]
