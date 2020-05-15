from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from games.models import Gamesimage, Games
from consoles.models import Console_brand_type

from consoles.models import Console_brand_type

from consoles.models import Consoles

from games.filters import ConsoleFilter

def get_game_by_id(request, id):
    context = {'game': get_object_or_404(Games, pk=id)}
    return render(request, 'games/game_details.html', context)


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        games = [ {
            'id'            : x.id,
            'name'          : x.name,
            'description'   : x.description,
            'firstImage'    : x.image
        } for x in Games.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': games})

    context = {'game_table': Games.objects.all()}
    return render(request, 'games/index.html', context)


def index_by_name(request):
    context = {'game_table': Consoles.objects.all().order_by('name')}
    return render(request, 'games/game_by_name.html', context)


def index_by_price(request):
    context = {'game_table': Consoles.objects.all().order_by('price')}
    return render(request, 'games/game_by_price.html', context)