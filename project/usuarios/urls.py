from django.urls import path

from .import views

app_name = "usuarios"

urlpatterns = [
    path("usuario/list", views.usuario_list, name="usuario_list"),
    path("", views.index, name="index"),

]