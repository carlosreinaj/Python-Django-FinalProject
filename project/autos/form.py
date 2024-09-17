from django import forms
from .models import Auto
from django.core.exceptions import ValidationError


class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'

    def clean_ano(self):
        ano = self.cleaned_data['ano']
        if ano < 1900:
            raise ValidationError('El año debe ser mayor a 1900.')
        return ano

    def clean_modelo(self):
        modelo = self.cleaned_data['modelo']
        if len(modelo) < 3:
            raise ValidationError('El modelo debe tener al menos 3 caracteres.')
        return modelo