from django.urls import path
from . import views

urlpatterns = [
    path('', views.criarcontacto, name='contactos'),
]