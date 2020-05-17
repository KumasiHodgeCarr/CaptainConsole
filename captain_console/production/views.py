from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from .models import Product, OrderItem, Order,BillingAddress
from forms import CheckoutForm


# Create your views here.

def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']

        products = [ {
            'id'            : x.id,
            'name'          : x.Product_name,
            'description'   : x.Product_description,
            'firstImage'    : x.Product_image,
            'price'         : x.Product_price,
            'platform'      : x.get_Product_platform_display,
            'category'      : x.get_Product_category_display

        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.all().order_by('Product_name') }
    return render(request, 'products/products.html', context)

def item_list(request):

    context = { 'items': Product.objects.all().order_by('Product_name')}
    return render(request, "products/products.html",context)

    context = { 'items': Product.objects.all()}
    return render(request, "products/products.html",context)
#def item_list(request):

#    context = { 'items': Product.objects.all().order_by('Product_name')}
#    return render(request, "products/products.html",context)

 #   context = { 'items': Product.objects.all()}
 #   return render(request, "products/products.html",context)



def index_by_price(request):
    context = {'items': Product.objects.all().order_by('price')}
    return render(request, 'products/products_by_price.html', context)

def order_by_console(request):
    context = {'console': Product.objects.all().filter(Product_category='C')}
    return render(request, 'products/products.html')

def order_by_games(request):
    context = {'game': Product.objects.all().filter(Product_category='G')}

class HomeView(ListView):
    model = Product
    paginate_by = 6
    template_name = "products/products.html"



class OrderSummaryView(View):
    def get(self, *args, **kwargs):

        return render(self.request, 'products/order-summary.html')

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


class CheckoutView(View):
    def get(self, *args, **kwargs):
        # form
        form = CheckoutForm()

        context = {
            'form': form
        }
        return render(self.request, 'products/checkout.html',context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('appartment_address')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                same_billing_address = form.cleaned_data.get(
                    'same_billing_address'
                )
                save_info = form.cleaned_data.get('save_info')
                patment_option = form.cleaned_data.get('payment_option')
                order.save()

                return redirect('production:checkout')
            messages.warning(self.request, "Failed checkout")
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect('production:checkout')


class ItemDetailView(DetailView):
    model = Product

    template_name = "products/product.html"

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Product,slug=slug)
    order_item = OrderItem.objects.get_or_create(item=item,
                                                 user=request.user,
                                                 ordered=False)

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request, "Item quantity updated")
            return redirect("production:product", slug=slug)

        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart")
            return redirect("production:product", slug=slug)
    else:
        order = Order.objects.create(user=request.user)
        user = request.user
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
        return redirect("production:product", slug =slug)

@login_required
def remove_from_cart(request,slug):
    item = get_object_or_404(Product, slug=slug)
    order_item = OrderItem.objects.get_or_create(item=item,
                                                 user=requset.user,
                                                 ordered=False)

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                    item = item,
                    user = request.user,
                    ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart")
            return redirect("production:product", slug=slug)

        else:
            messages.info(request, "This item was not in your cart")
            return redirect("production:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("production:product", slug=slug)
def checkout(request):
    return render(request, 'products/checkout.html')

class ItemDetailView(DetailView):
    model = Product
    template_name = "products/product.html"
