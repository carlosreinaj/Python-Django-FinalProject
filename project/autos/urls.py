from django.urls import path

from .import views

app_name = "autos"

urlpatterns = [
    path("autoscategorias/list", views.autoscategorias_list, name="autoscategorias_list"),
    path("", views.index, name="index"),
]