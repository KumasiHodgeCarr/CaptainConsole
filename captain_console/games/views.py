from django.shortcuts import render, get_object_or_404

from games.models import Gamesimage, Games

from consoles.models import Console_brand_type

from consoles.models import Consoles

from games.filters import ConsoleFilter

# consolepageconsoles =  [
#     { 'name': 'playstation1', 'description' : 'blah', 'brand' : 'sony', 'price' : 59.99 },
#     { 'name': 'Xbox', 'description' : 'blah', 'brand' : 'Xbox', 'price' : 59.99 },
#     { 'name': 'Nintendo', 'description' : 'blah', 'brand' : 'Nintendo', 'price' : 59.99 },
#     { 'name': 'PC', 'description' : 'blah', 'brand' : 'PC', 'price' : 59.99 }

# ]

# Create your views here.

# def index(request):
#     return render(request, 'games/index.html', context={
#         'gamepagegames': gamepagegames,
#         'consolepageconsoles': consolepageconsoles
#         })


def get_game_by_id(request, id):
    context = {'game': get_object_or_404(Games, pk=id)}
    return render(request, 'games/game_details.html', context)


def index(request):
    context = {'game_table': Games.objects.all().order_by('name')}
    return render(request, 'games/index.html', context)


def console_brand_view(request):
    context = {'console_brand' : Console_brand_type.objects.all().order_by('brand')}
    return render(request, 'games/game_details.html',context)


def brand_list(request):
    brand_list = Consoles.objects.all()
    brand_filter = ConsoleFilter(request.GET, queryset=brand_list)
    return render(request, 'games/index.html', {'filter': brand_filter})
