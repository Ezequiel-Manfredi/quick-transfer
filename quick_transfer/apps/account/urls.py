from django.urls import path

from .import views

app_name = 'account'

urlpatterns = [
  path('',views.Details.as_view(), name='home'),
  path('load/',views.Load.as_view(), name='load'),
  path('search/',views.Search.as_view(), name='search')
]