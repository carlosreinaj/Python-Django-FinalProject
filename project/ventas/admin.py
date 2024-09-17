from django.contrib import admin

from .models import Venta

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ("usuario", "producto", "cantidad", "precio_total", "fecha_venta")
    list_display_links = ("producto",)
    search_fields = ("producto.modelo", "usuario.nombre", "usuario.apellido")
    list_filter = ("usuario",)
    date_hierarchy="fecha_venta"
