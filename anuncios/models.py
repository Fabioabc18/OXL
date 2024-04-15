from django.db import models
from django.contrib.auth.models import User
from categorias.models import Categoria


class Anuncio(models.Model):
    titulo = models.CharField(max_length=150, blank=False, null=False)
    subtitulo = models.CharField(max_length=255, blank=False, null=False)
    preco = models.DecimalField(max_digits=10, decimal_places=3)
    data_post = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()
    id_utilizador = models.ForeignKey(User, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
