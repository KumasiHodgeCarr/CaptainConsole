from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name ='mybagindex'),
    path('checkout', views.checkout, name='checkout')
]
