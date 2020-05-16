from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name ='consoleindex'),
    path('name', views.index_by_name, name ='console_by_name'),
    path('price', views.index_by_price, name ='console_by_price'),


    path('<int:id>', views.get_console_by_id, name="console_details")

]