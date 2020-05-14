from django.shortcuts import render, get_object_or_404

from games.models import Gamesimage, Games

#from django import *

from consoles.models import Consoles
# gamepagegames =  [
#     { 'name': 'assassins creed', 'price' : 59.99 },
#     { 'name': 'fifa', 'price' : 59.99 },
#     { 'name': 'super mario', 'price' : 59.99 },
#     { 'name': 'skate 3', 'price' : 59.99 },
#     { 'name': 'skate 2', 'price' : 59.99 },
#     { 'name': 'fifa', 'price' : 59.99 },
#     { 'name': 'super mario', 'price' : 59.99 },
#     { 'name': 'skate 3', 'price' : 59.99 },
#     { 'name': 'assassins creed', 'price' : 59.99 },
#     { 'name': 'fifa', 'price' : 59.99 },
#     { 'name': 'super mario', 'price' : 59.99 }
# ]

# consolepageconsoles =  [
#     { 'name': 'playstation1', 'description' : 'blah', 'brand' : 'sony', 'price' : 59.99 },
#     { 'name': 'Xbox', 'description' : 'blah', 'brand' : 'Xbox', 'price' : 59.99 },
#     { 'name': 'Nintendo', 'description' : 'blah', 'brand' : 'Nintendo', 'price' : 59.99 },
#     { 'name': 'PC', 'description' : 'blah', 'brand' : 'PC', 'price' : 59.99 }

# ]

# Create your views here.

# def index(request):
#     context = { 'games': Games.objects.all() }
#     return render(request, 'games/index.html', context )

# def index(request):
#     return render(request, 'games/index.html', context={
#         'gamepagegames': gamepagegames,
#         'consolepageconsoles': consolepageconsoles
#         })

# def index(request):
#     context = {'games_slide': Games.objects.all()}
#     return render(request, 'games/index.html', context)


# def index(request):
#     context = {'consolepageconsoles': Consoles.objects.all()}
#     return render(request, 'games/index.html', context)


def get_game_by_id(request, id):
    context = {'game': get_object_or_404(Games, pk=id)}
    return render(request, 'games/game_details.html', context)


def index(request):
    context = {'game_table': Games.objects.all().order_by('name')}
    return render(request, 'games/index.html', context)

# def index2(request):
#     context = {'console_table': Consoles.objects.all()}
#     return render(request, 'games/index.html', context)
