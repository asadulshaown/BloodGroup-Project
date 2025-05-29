
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('create/', views.Registar, name='Registar'),
    path('display_data', views.display_data, name='display_data'),
    
]