from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("detalhesanuncio/<int:id>", views.detalhesanuncio, name="detalhesanuncio"),
    path("anuncios", views.anuncios, name="anuncios"),
  
   
]