
from django import forms

#from .models import Anuncio




class CriarContactoForm(forms.Form):
    full_name = forms.CharField(label="Primeiro Nome", max_length=200, required=True)
    email = forms.EmailField(label="E-mail", required=True)
    subject = forms.CharField(label="Assunto", max_length=200, required=True)
    message = forms.CharField(label="Mensagem", widget=forms.Textarea, required=True)





  

