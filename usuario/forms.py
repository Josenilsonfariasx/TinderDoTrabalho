from dataclasses import fields
from django import forms
from .models import usuario
class CriarUsuario(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['Pretencao_Salarial']