from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name ='item_list'),
    path('name', views.index_by_name, name ='product_by_name'),
    path('price', views.index_by_price, name ='product_by_price'),
]
