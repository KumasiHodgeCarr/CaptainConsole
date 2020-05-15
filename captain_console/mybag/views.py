from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mybag/index.html')

def checkout(request):
    return render(request, 'mybag/checkout.html')
