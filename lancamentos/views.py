from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from datetime import datetime

from lancamentos.forms import LancamentoForm
from lancamentos.models import Lancamento
from tipolancamentos.models import TipoLancamento


def index(request):
    lancamentos = Lancamento.objects.filter(tipo="CX")
    return render(request, "lancamento/index.html", context={"lancamentos": lancamentos})


def create(request):
    lancamentos = TipoLancamento.objects.all()
    return render(request=request, template_name="lancamento/create.html", context={"tipos": lancamentos})


def store(request):
    if request.method == 'POST':
        form = LancamentoForm(request.POST)
        if form.is_valid():
            lancamento = Lancamento()
            lancamento.data = datetime.strptime(request.POST['data'], "%d/%m/%Y").strftime('%Y-%m-%d')
            lancamento.descricao = request.POST['descricao']
            lancamento.tipo_lancamento = TipoLancamento.objects.get(id=int(request.POST['tipo_lancamento']))
            lancamento.classificacao = request.POST['classificacao']
            lancamento.tipo = request.POST['tipo']
            lancamento.valor = request.POST['valor']
            lancamento.observacoes = request.POST['observacoes']
            messages.success(request, "Lançamento Cadastrado com Sucesso!")
            lancamento.save()

    return redirect(reverse('fluxo_caixa_home'))


def edit(request, lancamento_id):
    lancamento = get_object_or_404(Lancamento, pk=lancamento_id)
    initial_form = {
        "data": lancamento.data,
        "descricao": lancamento.descricao,
        "valor": lancamento.valor,
        "tipo_lancamento": lancamento.tipo,
        "classificacao": lancamento.classificacao,
        "observacoes": lancamento.observacoes

    }

    lancamentos = TipoLancamento.objects.all()
    form = LancamentoForm(initial=initial_form)
    context = {"lancamento": lancamento, 'form': form, "tipos": lancamentos}
    return render(request, "lancamento/edit.html", context)


def update(request):
    if request.method == 'POST':
        form = LancamentoForm(request.POST)
        if form.is_valid():
            print('Sucesso')
            lancamento = Lancamento.objects.get(pk=request.POST['id_lancamento'])
            lancamento.data = request.POST['data']
            lancamento.descricao = request.POST['descricao']
            lancamento.tipo_lancamento = TipoLancamento.objects.get(id=int(request.POST['tipo_lancamento']))
            lancamento.classificacao = request.POST['classificacao']
            lancamento.tipo = request.POST['tipo']
            lancamento.valor = request.POST['valor']
            lancamento.observacoes = request.POST['observacoes']
            messages.success(request, "Lançamento Atualizado com Sucesso!")
            lancamento.save()

    return redirect(reverse('fluxo_caixa_home'))


def delete(request, lancamento_id):
    lancamento = get_object_or_404(Lancamento, pk=lancamento_id)
    lancamento.delete()
    messages.success(request, "Lancamento Excluído com Sucesso!")
    return redirect(reverse('fluxo_caixa_home'))
