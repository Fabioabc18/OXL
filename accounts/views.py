from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User




def signup(request):
    template = loader.get_template("registration/signup.html")
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        email = request.POST.get("email")
        try:
            
            if form["password1"].value() == form["password2"].value():
                user = User.objects.create_user(username=form["username"].value(
            ), password=form["password1"].value(), email=email)
            else:
                context = {
                "form": form,
                "message": "Passwords diferentes!"
            }
                return HttpResponse(template.render(context, request))

        except:
            context = {
                "form": form,
                "message": "Ocorreu um erro!"
            }
            return HttpResponse(template.render(context, request))

        return redirect("/")
    else:
        form = UserCreationForm()
       
        context = {
            "form": form
        }
        return HttpResponse(template.render(context, request))
