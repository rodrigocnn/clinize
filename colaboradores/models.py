from django.db import models


class Colaborador(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    cargo = models.ForeignKey("cargos.Cargo", on_delete=models.SET_NULL, null=True)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=20, blank=True)
    rg = models.CharField(max_length=20)
    email = models.CharField(max_length=100, blank=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    observacoes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
