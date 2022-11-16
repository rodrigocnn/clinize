from django.db import models


class Lancamento(models.Model):
    TYPE = (('CP', 'Contas a Pagar',), ('CR', 'Contas a Receber'), ('CX', 'Caixa'))
    TYPE_CLASSIFICATION = (('D', 'Despesa',), ('R', 'Receita'))
    data = models.DateField()
    descricao = models.CharField(max_length=100, unique=True)
    tipo_lancamento = models.ForeignKey("tipolancamentos.TipoLancamento", on_delete=models.CASCADE)
    classificacao = models.CharField(max_length=2, choices=TYPE_CLASSIFICATION, default="D")
    tipo = models.CharField(max_length=2, choices=TYPE)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    observacoes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
