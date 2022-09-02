from django.forms import Form, CharField, IntegerField

class FormularioBusqueda(Form):
    producto = CharField(max_length=150)

class FormularioProducto(Form):
    nombre_producto = CharField(max_length=150)
    precio = CharField(max_length=150)

class FormularioIntegrantes(Form):
    nombre = CharField (max_length=150)
    edad = IntegerField ()
    profesion = CharField(max_length=150)

class FormularioSucursales(Form):
    nombre_sucursal = CharField(max_length=150)
    direccion = CharField(max_length=150)
    dias = CharField(max_length=150)
    horarios = CharField(max_length=150) 
