from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name ='consoleindex'),
    path('<int:id>', views.get_console_by_id, name="console_details")

]