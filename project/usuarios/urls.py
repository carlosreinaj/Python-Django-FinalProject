from django.urls import path

from .import views

urlpatterns = [
    path("usuario/list", views.usuario_list),
]