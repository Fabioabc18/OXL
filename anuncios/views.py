from django.http import HttpResponse
from django.template import loader
from .models import Anuncio
from .models import Categoria
from .forms import CriarAnuncioForm


def anuncios(request):
    template = loader.get_template("anuncios.html")
    todosanuncios = Anuncio.objects.all()

    context = {
        "anuncios" : todosanuncios
    }

    return HttpResponse (template.render(context, request))


def criaranuncio(request):

    template = loader.get_template("criaranuncio.html")
    
    if request.method == 'POST':

        form = CriarAnuncioForm(request.POST)

        anuncio = Anuncio()
        
        anuncio.titulo = form["titulo"].value()
        anuncio.subtitulo = form["subtitulo"].value()
        anuncio.preco = form["preco"].value()
        anuncio.descricao = form["descricao"].value()

        anuncio.id_categoria = Categoria.objects.get(id=form["categoria"].value())
        anuncio.id_utilizador = request.user

        anuncio.save()
        

        context = {
            "form" : form,
            "message" : "Anuncio Publicado!"
        }

        return HttpResponse (template.render(context, request))
    
    else:
        form = CriarAnuncioForm()
        context = {
            "form" : form
        }
        return HttpResponse (template.render(context, request))
    


def detalhesanuncio(request, id):
    template = loader.get_template("detalhesanuncio.html")
    detalhes = Anuncio.objects.get(id=id)


    context = {
        "anuncio" : detalhes,
    }

    return HttpResponse (template.render(context, request))

