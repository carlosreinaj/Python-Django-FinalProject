from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatares", blank=True, null=True)


    def __str__(self):
        return f"{self.nombre} {self.apellido}"
