from games.models import Gamesimage
from consoles.models import Console_brand_type



def Games_images(request):
    context = {'games_slide': Gamesimage.objects.all()}
    return (context)

def console_brand_view(request):
    context = {'console_brand' : Console_brand_type.objects.all()}
    return (context)



