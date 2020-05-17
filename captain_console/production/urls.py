from django.urls import path
from . import views
from .views import ItemDetailView, CheckoutView, add_to_cart, remove_from_cart, HomeView, OrderSummaryView

app_name = 'production'

urlpatterns = [
    path('item-list', views.item_list, name ='item_list'),
    path('name', views.index_by_name, name ='product_by_name'),
    path('price', views.index_by_price, name ='product_by_price'),
    path('', HomeView.as_view(), name ='products'),
    path('checkout/',CheckoutView.as_view(),name='checkout'),
    path('order-summary/',OrderSummaryView.as_view(),name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/',add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/',remove_from_cart, name='remove-from-cart')
]
