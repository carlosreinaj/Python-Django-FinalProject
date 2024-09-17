from django.contrib import admin

from .import models

#admin.site.register(models.Usuario)

@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "correo", "telefono", "fecha_nacimiento")
    search_fields = ("nombre",)
    ordering = ("nombre",)