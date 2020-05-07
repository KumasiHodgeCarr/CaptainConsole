from django.shortcuts import render
from games.models import Gamesimage
from consoles.models import ConsolesImage


def Games_images(request):
    context = {'games_slide': Gamesimage.objects.all()}
    return (context)


