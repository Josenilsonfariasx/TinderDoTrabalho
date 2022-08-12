from django.db import models
from datetime import date
# Create your models here.
class Administrador(models.Model):
    email = models.CharField(max_length=100, null=True)
    senha = models.CharField(max_length=64, null=True)

    def __str__(self) -> str:
        return self.email
