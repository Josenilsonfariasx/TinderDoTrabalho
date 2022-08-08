from django.db import models
from usuario.models import usuario

class Vagas(models.Model):
    faixa_CHOICES = (("1k", "Ate 1k"),
                     ("1-2", "2k a 3K"),
                     ("2-3", "2k a 3k"),
                     ("3+", "Acima de 3k")
                     )

    escolaridade_CHOICES = (("Ensino fundamental", "Ensino Fundamental"),
                            ("Ensino Medio", "Ensino Medio"),
                            ("Tecnologo ", "Tecnólogo"),
                            ("Ensino Superior", "Ensino Superior"),
                            ("POS", " Pós / MBA / Mestrado"),
                            ("Doutorado", "Doutorado")
                     )

    nome = models.CharField(max_length = 100)
    descricao = models.TextField(max_length=2000)
    faixa_salarial = models.CharField(max_length=5,choices=faixa_CHOICES )
    requisitos = models.TextField(max_length=100)
    escolaridade = models.CharField(max_length=50, choices=escolaridade_CHOICES, null=True)
    class Meta:
        verbose_name = 'Vaga'
    def __str__(self):
        return self.nome