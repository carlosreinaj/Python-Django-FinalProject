from django.urls import path


from .import views

app_name = "usuarios"

urlpatterns = [
    path("", views.index, name="index"),
    #path("usuario/list", views.usuario_list, name="usuario_list"),
    path("usuario/list", views.UsuarioList.as_view(), name="usuario_list"),
    #path("usuario/create", views.usuario_create, name="usuario_create"),
    path("usuario/create", views.UsuarioCreate.as_view(), name="usuario_create"),
    #path("usuario/detail/<int:pk>", views.usuario_detail, name="usuario_detail"),
    path("usuario/detail/<int:pk>", views.UsuarioDeatil.as_view(), name="usuario_detail"),
    #path("usuario/update/<int:pk>", views.usuario_update, name="usuario_update"),
    path("usuario/update/<int:pk>", views.UsuarioUpdate.as_view(), name="usuario_update"),
    #path("usuario/delete/<int:pk>", views.usuario_delete, name="usuario_delete"),
    path("usuario/delete/<int:pk>", views.UsuarioDelete.as_view(), name="usuario_delete"),

]