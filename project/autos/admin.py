from django.contrib import admin

from .import models
#admin.site.register(AutosCategorias)
#admin.site.register(Auto)

@admin.register(models.Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ("modelo", "estado", "ano", "color", "precio")
    search_fields = ("modelo", "estado",)
    ordering = ("modelo",)