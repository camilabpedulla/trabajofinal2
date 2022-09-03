from django.shortcuts import render, redirect
from Mensajes.models import Mensajes
from Mensajes.forms import FormularioMensajes
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.

def mensajeria(request):
    
    mensajes = Mensajes.objects.all()
    
    return render(request, "Mensajes/mensajes.html", {"mensajes" : mensajes})

@login_required
def mensaje_nuevo(request):

    if request.method == "GET":
        formulario = FormularioMensajes({"emisor" : request.user.username})
        return render (request, "Mensajes/form_mensaje.html", {"formulario":formulario})


    else:

        formulario = FormularioMensajes(request.POST)

        if formulario.is_valid(): 

            data = formulario.cleaned_data
           
            texto = data.get("texto_mensaje")
            emisor = data.get("emisor_mensaje")
            receptor = data.get("receptor_mensaje")
            mensaje = Mensajes(texto=texto, emisor=emisor , receptor=receptor)
        
            mensaje.save()

            return redirect("mensajeria")
        
        else:
            
            return HttpResponse(f"La informacion ingresada no es valida")

