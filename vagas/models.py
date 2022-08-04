from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
class Vagas(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField(max_length=2000)
    faixa_salarial = models.TextField(max_length=3)
    requisitos = models.TextField(max_length=100)
    escolaridade = models.CharField(max_length=50, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        verbose_name = 'Vaga'
    def __str__(self):
        return self.nome