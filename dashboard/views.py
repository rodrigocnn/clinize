from django.shortcuts import render
from lancamentos.models import Lancamento
from django.db.models import Sum


def index(request):
    receitas = Lancamento.objects.filter(tipo="CX", classificacao="R")
    despesas = Lancamento.objects.filter(tipo="CX", classificacao="D")
    totalR = receitas.aggregate(Sum('valor'))['valor__sum']
    totalD = despesas.aggregate(Sum('valor'))['valor__sum']
    saldo = totalR - totalD
    return render(request, "dashboard/index.html",  context={"receitas": totalR, "despesas": totalD, "saldo": saldo})
