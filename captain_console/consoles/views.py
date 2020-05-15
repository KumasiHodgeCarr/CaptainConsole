from django.shortcuts import render, get_object_or_404
from consoles.models import Consoles



# Create your views here.


def get_console_by_id(request, id):
    context = {'console': get_object_or_404(Consoles, pk=id)}
    return render(request, 'consoles/console_details.html', context)

def index(request):
    context = {'console_table': Consoles.objects.all()}
    return render(request, 'consoles/index.html', context)


def index_by_name(request):
    context = {'console_table': Consoles.objects.all().order_by('name')}
    return render(request, 'consoles/console_by_name.html', context)


def index_by_price(request):
    context = {'console_table': Consoles.objects.all().order_by('price')}
    return render(request, 'consoles/console_by_price.html', context)


