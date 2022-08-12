from django.db import models
from usuario.models import usuario

class Vagas(models.Model):
    faixa_CHOICES = (("ate 1k", "Ate 1k"),
                     ("1k a 2k", "1k a 2k"),
                     ("2k a 3k", "2k a 3K"),
                     ("3k+", "Acima de 3k"),
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
    faixa_salarial = models.CharField(max_length=10,choices=faixa_CHOICES )
    requisitos = models.TextField(max_length=2000)
    escolaridade = models.CharField(max_length=50, choices=escolaridade_CHOICES, null=True)
    candidatos = models.ManyToManyField(usuario, related_name='Vagas')

    def setCandidato(self, candidato_input):
        self.candidatos.add(candidato_input)

    class Meta:
        verbose_name = 'Vaga'
    def __str__(self):
        return self.nome