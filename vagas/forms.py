from dataclasses import fields
from django import forms
from .models import Vagas
class CriarVaga(forms.ModelForm):
    class Meta:
        model = Vagas
        fields = ['nome', 'descricao', 'faixa_salarial', 'requisitos', 'escolaridade']
