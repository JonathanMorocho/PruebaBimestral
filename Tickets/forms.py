from django import forms
from .models import Usuarios

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'
