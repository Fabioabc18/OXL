from django.db import models
from django.contrib.auth.models import User

class Contacto(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    id_utilizador = models.ForeignKey(User, on_delete=models.CASCADE)

    



