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
        
        
    def clean_numero(self):
        numero = self.cleaned_data.get("numero", "")
        
        if not numero.isdigit():
            raise ValidationError("El número solo puede contener dígitos")
        
        return numero
