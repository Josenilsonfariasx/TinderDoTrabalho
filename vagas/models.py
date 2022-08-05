from django.db import models
from usuario.models import usuario

class Vagas(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField(max_length=2000)
    faixa_salarial = models.TextField(max_length=10)
    requisitos = models.TextField(max_length=100)
    escolaridade = models.CharField(max_length=50, null=True)
    class Meta:
        verbose_name = 'Vaga'
    def __str__(self):
        return self.nome