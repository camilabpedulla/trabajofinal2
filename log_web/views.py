from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from log_web.forms import Customizacion_usuario
from django.contrib.auth.mixins import LoginRequiredMixin
from log_web.forms import UserEditForm, AvatarForm
from django.contrib.auth.decorators import login_required
from log_web.models import Avatar
from django.contrib.auth.models import User

# Create your views here.



def iniciar_sesion (request):

    if request.method == "GET":

        formulario = AuthenticationForm()
        context =  {
            "formulario":formulario
           
            }
        return render (request, "log_web/login.html", context)

    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = authenticate(username=data.get("username"), password=data.get("password"))

            if usuario is not None:
                login(request, usuario)
                return redirect ("avatar")

            else:
                context =  {
            "error": "Credenciales no validas",
            "formulario": formulario
            }
            return render (request, "log_web/login.html", context)

        else: 
            context =  {
            "error": "Formulario no valido",
            "formulario": formulario
            }
            return render (request, "log_web/login.html", context)


      
def registrar_usuario (request):
    if request.method == "GET":
        formulario = Customizacion_usuario()
        return render (request, "log_web/registro.html",{"formulario":formulario})

    else:
        formulario = Customizacion_usuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect ("/WebPage/inicio")
        else:
          return render (request, "log_web/registro.html",{"formulario":formulario, "error": "Formulario no valido"})
        

@login_required
def editar_usuario (request):

    if request.method == "GET":

        form = UserEditForm(initial = {"email" : request.user.email, "first_name" : request.user.first_name, "last_name" : request.user.last_name })

        return render (request, 'log_web/update_user.html', {"form" : form})



    else:

        form = UserEditForm(request.POST)

        if form.is_valid(): 

            data = form.cleaned_data
           
            usuario = request.user
            usuario.email = data["email"]
            usuario.password1= data["password1"]
            usuario.password2 = data["password2"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
           

            usuario.save()

            return redirect("inicio")
        
        else:
            
            return render(request, 'log_web/update_user.html', {"form" : form})
        


def avatar (request):
       
        if not request.user.is_anonymous:
            avatar = Avatar.objects.filter(usuario=request.user). last()
            contexto = {"imagen": avatar.imagen.url}

        return render (request, "log_web/avatar.html", contexto)



@login_required
def agregar_avatar(request):

    if request.method == "GET":
        form = AvatarForm()
        contexto = {"form": form}
        return render(request, "log_web/agregar_avatar.html", contexto)
    else:
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            usuario = User.objects.filter(username=request.user.username).first()
            avatar = Avatar(usuario=usuario,imagen=data["imagen"])
            print(usuario)
            print(data)

            avatar.save()
            return redirect("inicio")
        contexto = {"form": form, }
        return render(request, "log_web/avatar.html", contexto)
        

 







    


