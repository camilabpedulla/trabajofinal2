from django.urls import path
from Mensajes.views import *
from Mensajes.views import mensaje_nuevo, mensajeria

urlpatterns = [
    path('', mensaje_nuevo, name="mensaje"),
    path('mensajes/', mensajeria, name="mensajeria")
    
]