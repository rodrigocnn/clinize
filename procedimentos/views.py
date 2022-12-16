from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages

from procedimentos.forms import ProcedimentoForm
from procedimentos.models import Procedimento


def index(request):
    procedimentos = Procedimento.objects.all()
    return render(request, "procedimentos/index.html", context={"procedimentos": procedimentos})


def create(request):
    form = ProcedimentoForm()
    context = {'form': form}
    return render(request, "procedimentos/create.html", context)


def store(request):
    if request.method == 'POST':
        form = ProcedimentoForm(request.POST)
        if form.is_valid():
            procedimento = Procedimento()
            procedimento.descricao = request.POST['descricao']
            procedimento.valor = request.POST['valor']
            procedimento.save()
            messages.success(request, "Procedimento Cadastrado com Sucesso!")

    return redirect(reverse('procedimentos_home'))


def edit(request, procedimento_id):
    procedimento = get_object_or_404(Procedimento, pk=procedimento_id)
    initial_form = {"descricao": procedimento.descricao, "valor": procedimento.valor}
    form = ProcedimentoForm(initial=initial_form)
    context = {"procedimento": procedimento, 'form': form}
    return render(request, "procedimentos/edit.html", context)


def update(request):
    if request.method == 'POST':
        form = ProcedimentoForm(request.POST)
        if form.is_valid():
            procedimento = Procedimento.objects.get(pk=request.POST['id_procedimento'])
            procedimento.descricao = request.POST['descricao']
            procedimento.valor = request.POST['valor']
            messages.success(request, "Procedimento Atualizado com Sucesso!")
            procedimento.save()
            return redirect(reverse('procedimentos_home'))


def delete(request, procedimento_id):
    procedimento = get_object_or_404(Procedimento, pk=procedimento_id)
    procedimento.delete()
    messages.success(request, "Procedimento Excluído com Sucesso!")
    return redirect(reverse('procedimentos_home'))
