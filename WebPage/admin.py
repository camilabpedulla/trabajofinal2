from django.contrib import admin
from WebPage.models import Productos, Integrantes, Sucursales
from log_web.models import Avatar

# Register your models here.

admin.site.register(Productos)
admin.site.register(Integrantes)
admin.site.register(Sucursales)

