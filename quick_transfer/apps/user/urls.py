from django.urls import path
from django.contrib.auth import views as views_django

from .import views

app_name = 'user'

urlpatterns = [
    path('login/', views_django.LoginView.as_view(template_name="user/login.html"), name="login"),
    path('signup', views.NewUser.as_view(), name='signup'),
    path('logout/', views_django.logout_then_login, name="logout"),
]