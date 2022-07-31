from django.db import models

class Vagas(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField(max_length=2000)
    faixa_salarial = models.TextField(max_length=20)
    requisitos = models.TextField(max_length=100)

    class Meta:
        verbose_name = 'Vaga'
    def __str__(self):
        return self.nome

