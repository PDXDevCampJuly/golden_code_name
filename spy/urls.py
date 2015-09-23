from django.conf.urls import url
from .views import GameBoardList

urlpatterns = [
    url(r'^$', GameBoardList.as_view())
]
