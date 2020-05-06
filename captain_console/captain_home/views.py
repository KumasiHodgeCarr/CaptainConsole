from django.shortcuts import render
from captain_home.models import HomeMainImage

# Create your views here.


def index(request):
    return render(request, 'captainconsole/index.html')