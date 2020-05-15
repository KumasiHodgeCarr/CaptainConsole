from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product
# Create your views here.


def item_list(request):
    context = { 'items': Product.objects.all()}
    return render(request, "products/products.html",context)