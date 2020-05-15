from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name ='gamesindex'),
    path('name', views.index_by_name, name ='game_by_name'),
    path('price', views.index_by_price, name ='game_by_price'),
    path('<int:id>', views.get_game_by_id, name="game_details"),
    # path(r"^search/$", views.brand_list, name="games")

]

