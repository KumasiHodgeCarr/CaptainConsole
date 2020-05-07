from games.models import Gamesimage



def Games_images(request):
    context = {'games_slide': Gamesimage.objects.all()}
    return (context)


