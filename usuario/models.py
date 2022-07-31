from django.db import models

class usuario(models.Model):
    
    nome = models.CharField(max_length= 35)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=64)
    idade = models.CharField(max_length=4)



    def __str__(self) -> str:
        return self.nome