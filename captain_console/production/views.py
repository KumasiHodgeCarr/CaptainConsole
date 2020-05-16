from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product
# Create your views here.


#def item_list(request):

#    context = { 'items': Product.objects.all().order_by('Product_name')}
#    return render(request, "products/products.html",context)

 #   context = { 'items': Product.objects.all()}
 #   return render(request, "products/products.html",context)



#def index_by_name(request):
#    context = {'items': Product.objects.all().order_by('name')}
#    return render(request, 'products/products_by_name.html', context)


#def index_by_price(request):
 #   context = {'items': Product.objects.all().order_by('price')}
 #   return render(request, 'products/products_by_price.html', context)


def products(request):
    context = {
        'items': Product.objects.all()
    }
    return render(request, 'products/products.html',context)

def checkout(request):
    return render(request, 'products/checkout.html')

class ItemDetailView(DetailView):
    model = Product
    template_name = "products/product.html"