from django.db import models

class AutosCategorias(models.Model):
    tipo = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'Categoria de Auto'
        verbose_name_plural ='Categorias de Autos'