from django.urls import path

from django.contrib.auth.decorators import login_required


from .import views

app_name = "autos"




urlpatterns = [
    path("", views.index, name="index"),
    #path("autos/list", views.autos_list, name="autos_list"),
    path("autos/list", login_required(views.AutoList.as_view()), name="autos_list"),
    #path("autos/create", views.autos_create, name="autos_create"),
    path("autos/create", login_required(views.AutoCreate.as_view()), name="autos_create"),
    #path("autos/detail/<int:pk>", views.autos_detail, name="autos_detail"),
    path("autos/detail/<int:pk>", login_required(views.AutoDeatil.as_view()), name="autos_detail"),
    #path("autos/update/<int:pk>", views.autos_update, name="autos_update"),
    path("autos/update/<int:pk>", login_required(views.AutoUpdate.as_view()), name="autos_update"),
    #path("autos/delete/<int:pk>", views.autos_delete, name="autos_delete"),
    path("autos/delete/<int:pk>", login_required(views.AutoDelete.as_view()), name="autos_confirm_delete"),
]