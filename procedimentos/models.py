from django.db import models


class Procedimento(models.Model):

    descricao = models.CharField(max_length=100, unique=True)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
