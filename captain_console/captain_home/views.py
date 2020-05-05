from django.shortcuts import render

homepageimage =  [
    { 'name': 'Call of Duty: Warzone', 'price' : 0 }
]

# Create your views here.
def index(request):
    return render(request, 'captainconsole/index.html', context={
        'homepageimage': homepageimage
    })
