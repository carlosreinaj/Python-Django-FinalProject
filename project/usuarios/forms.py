from django import forms
from django.core.exceptions import ValidationError

from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario 
        fields = '__all__'

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre", "")

        if not nombre.isalpha():
            raise ValidationError("El nombre solo puede contener letras")
        
        return nombre
        
    def clean_apellido(self):
        apellido = self.cleaned_data.get("apellido", "")

        if not apellido.isalpha():
            raise ValidationError("El apellido solo puede contener letras")
        
        return apellido
        
        
    def clean_telefono(self):  # Cambiado de 'numero' a 'telefono'
        telefono = self.cleaned_data.get("telefono", "")
        if not telefono.isdigit():
            raise ValidationError("El numero solo puede contener dígitos")
        return telefono
