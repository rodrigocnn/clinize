from django.db import models


class TipoLancamento(models.Model):
    TYPE_CHOICES = (('D', 'Despesa',), ('R', 'Receita'))
    descricao = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=10, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
