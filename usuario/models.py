from django.db import models

#from vagas.models import Vagas

class usuario(models.Model):
    Pretencao_Salarial_CHOICES = (("ate 1k", "Ate 1k"),
                     ("1k a 2k", "1k a 2k"),
                     ("2k a 3k", "2k a 3K"),
                     ("3k+", "Acima de 3k"),
                     )


    nome = models.CharField(max_length= 35)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=64)
    Pretencao_Salarial = models.CharField(max_length=10,choices=Pretencao_Salarial_CHOICES, null=True)

    def __str__(self) -> str:
        return self.nome