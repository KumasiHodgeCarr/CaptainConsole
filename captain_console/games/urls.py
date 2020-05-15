from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name ='gamesindex'),
    path('<int:id>', views.get_game_by_id, name="game_details"),
    # path(r"^search/$", views.brand_list, name="games")

]

