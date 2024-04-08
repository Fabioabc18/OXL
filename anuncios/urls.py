from django.urls import path
from . import views

urlpatterns = [
    path('', views.anuncios, name='anuncios'),
    path('criaranuncio', views.criaranuncio, name="criaranuncio"),
    path("detalhesanuncio/<int:id>", views.detalhesanuncio, name="detalhesanuncio"),
]