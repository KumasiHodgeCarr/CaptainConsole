from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register' ),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout',LogoutView.as_view(next_page='homeindex'), name='logout'),
    path('profile',views.profile, name='profile'),
    path('changepassword', views.change_password, name='change_password'),
]

