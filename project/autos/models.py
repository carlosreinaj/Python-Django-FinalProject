from django.db import models

class AutosCategorias(models.Model):
    ESTADO_CHOICES = [
        ('Nuevo', 'Nuevo'),
        ('Usado', 'Usado')
    ]
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Nuevo')
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = 'Categoria de Auto'
        verbose_name_plural ='Categorias de Autos'

class Auto(models.Model):
    estado = models.ForeignKey(AutosCategorias, on_delete=models.SET_NULL, null=True, blank=True)
    modelo = models.CharField(max_length=50)
    ano = models.PositiveIntegerField()
    COLOR_CHOICES = [
        ('Rojo', 'Rojo'),
        ('Azul', 'Azul'),
        ('Negro', 'Negro'),
        
    ]
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.FloatField()
    fecha_actualizacion = models.DateField(editable=False, auto_now=True)

    def __str__(self):
        return f"{self.modelo} {self.color} ({self.ano}) | {self.estado}"

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural ='Autos'
        constraints = [
            models.UniqueConstraint(fields=['modelo', 'ano'], name='modelo_ano')
        ]
        # La siguiente línea es para crear un índice en la base de datos
        # Un ínidice es una estructura de datos que mejora la velocidad de búsqueda
        indexes = [models.Index(fields=['modelo'])]

    def disminuir_stock(self, cantidad):
        """cantidad es enviado desde el modelo Venta"""
        if self.stock >= cantidad:
            self.stock -= cantidad
            self.save()
        else:
            raise ValueError('No hay suficiente stock disponible')


    def aumentar_stock(self, cantidad):
        self.stock += cantidad
        self.save()