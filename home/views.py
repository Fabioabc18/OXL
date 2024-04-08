from django.http import HttpResponse
from django.template import loader
from anuncios.models import Anuncio

#from django.core.mail import send_mail


def home(request):
    template = loader.get_template("home.html")
    todosanuncios = Anuncio.objects.all()

    context = {
        "anuncios" : todosanuncios
    }

    return HttpResponse (template.render(context, request))


def detalhesanuncio(request, id):
    template = loader.get_template("detalhesanuncio.html")
    detalhes = Anuncio.objects.get(id=id)


    context = {
        "anuncio" : detalhes,
    }

    return HttpResponse (template.render(context, request))


def anuncios(request):
    template = loader.get_template("anuncios.html")
    todosanuncios = Anuncio.objects.all()

    context = {
        "anuncios" : todosanuncios
    }

    return HttpResponse (template.render(context, request))



