from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=150)
    email = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome