from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from .forms import CriarContactoForm
from .models import Contacto

def criarcontacto(request):
    template = loader.get_template('contactos.html')
    form = CriarContactoForm()

    if request.method == 'POST':
        form = CriarContactoForm(request.POST)
        if form.is_valid():
            contacto = Contacto(
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            contacto.id_utilizador = request.user
            contacto.save()

            subject = 'Agradecemos o seu contacto'
            message = 'Agradecemos o seu contacto, entraremos em contacto o mais breve possível, obrigado pela sua preferência!'
            sender_email = 'fabioabc18@sapo.pt'
            recipient_list = [form.cleaned_data['email']]
            send_mail(subject, message, sender_email, recipient_list)

           
            form = CriarContactoForm()

            context = {
                'form': form,
                'message': 'Formulário enviado com sucesso, em breve receberá um email de confirmação!'
            }
            return HttpResponse(template.render(context, request))

    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))
