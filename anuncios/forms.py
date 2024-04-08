
from django import forms
from categorias.models import Categoria
from django.forms import ModelChoiceField
#from .models import Anuncio


class CategoriaModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
         return f"{obj.name}"



class CriarAnuncioForm(forms.Form):
    titulo = forms.CharField(label="Título", max_length=200, required=True)
    subtitulo = forms.CharField(label="Sub-Título", max_length=255, required=True)
    preco = forms.DecimalField(max_digits=10, decimal_places=2)
    descricao = forms.CharField(label="Descrição", max_length=255, required=True)
    categoria = CategoriaModelChoiceField(queryset=Categoria.objects.all(),required=True,empty_label="Seleciona uma categoria")


