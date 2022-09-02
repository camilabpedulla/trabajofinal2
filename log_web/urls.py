
from django.urls import path
from log_web.views import iniciar_sesion, registrar_usuario, editar_usuario, agregar_avatar, avatar
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('iniciar_sesion/', iniciar_sesion, name="Iniciar"),
    path('registrar_usuario/', registrar_usuario, name="Registrarse"),
    path('cerrar_sesion/', LogoutView.as_view(template_name= "log_web/logout.html"), name="cerrar_sesion"),
    path('editar/', editar_usuario, name = "editar_usuario"),
    path('avatar/', avatar, name="avatar"),
    path("agregar_avatar/", agregar_avatar, name="agregar_avatar")
]

# Para acceder a las imagenes desde el navegador

