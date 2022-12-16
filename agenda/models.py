from django.db import models


class Agenda(models.Model):

    title = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    paciente = models.ForeignKey("pacientes.Paciente", on_delete=models.CASCADE)
    colaborador = models.ForeignKey("colaboradores.Colaborador", on_delete=models.CASCADE)
    procedimento = models.ForeignKey("procedimentos.Procedimento", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
