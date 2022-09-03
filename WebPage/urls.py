from django.urls import path
from WebPage.views import *
from WebPage.views import lista_productos, crear_prod, detalle_prod, editar_prod, borrar_prod

urlpatterns = [
    path('', inicio, name="Tienda_Olivia"),
    path('productos/', productos, name="inicio"),
    path('integrantes/', integrantes, name="integrantes"),
    path('sucursales/', sucursales, name="sucursales"),
    path('productos/carga', productos_carga, name="carga_productos"),
    path('integrantes/carga/', integrantes_carga, name="carga_integrantes"),
    path('sucursales/carga/', sucursales_carga, name ="carga_sucursales"),
    path('login/', login, name = 'Login'),
    
    
    
    
    path('productos/lista', lista_productos.as_view(), name = "lista_productos"),
    path('productos/crear/', crear_prod.as_view(), name = 'crear_producto' ),
    path('productos/editar/<pk>', editar_prod.as_view(), name = 'editar_producto' ),
    path('productos/borrar/<pk>', borrar_prod.as_view(), name = 'borrar_producto' ),
    path('productos/<pk>', detalle_prod.as_view(), name = 'detalle_producto' ),
    
]


