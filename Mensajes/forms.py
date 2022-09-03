from django.forms import Form, CharField, DateTimeField


class FormularioMensajes(Form):
    texto_mensaje = CharField(max_length=500)
    emisor_mensaje = CharField(max_length=150)
    receptor_mensaje = CharField(max_length=150)
    
