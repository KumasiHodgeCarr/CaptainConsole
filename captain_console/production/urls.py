from django.urls import path
from . import views
from .views import ItemDetailView,checkout

app_name = 'production'

urlpatterns = [
    #path('', views.item_list, name ='item_list'),
#    path('name', views.index_by_name, name ='product_by_name'),
  #  path('price', views.index_by_price, name ='product_by_price'),
    path('', views.products, name ='products'),
    path('checkout/',checkout,name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product')
]
