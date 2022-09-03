from django.forms import  CharField, EmailField, PasswordInput, ImageField, Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Customizacion_usuario(UserCreationForm):
    email = EmailField ()
    password1= CharField (label="Contraseña", widget=PasswordInput)
    password2= CharField (label="Confirmar Contraseña", widget=PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {"username": "", "email": "", "password1": "", "password2": ""}



class UserEditForm(UserCreationForm):

    email = EmailField ()
    password1= CharField (label="Contraseña", widget=PasswordInput)
    password2= CharField (label="Confirmar Contraseña", widget=PasswordInput)
    first_name = CharField ( label = "Nombre")
    last_name = CharField ( label = "Apellido")
   

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]
        help_texts = {"email": "", "password1": "", "password2": ""}

class AvatarForm(Form):
    imagen = ImageField()
