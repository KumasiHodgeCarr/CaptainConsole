from django.urls import path
from . import views

urlpatterns = [
    path('captainhome', views.index, name='homeindex'),
]
