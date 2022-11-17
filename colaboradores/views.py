from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from datetime import datetime

from cargos.models import Cargo
from colaboradores.forms import ColaboradorForm
from colaboradores.models import Colaborador


@login_required
def index(request):
    coloaboradores = Colaborador.objects.all()
    return render(request, "colaboradores/index.html", context={"colaboradores": coloaboradores})


@login_required
def create(request):
    cargos = Cargo.objects.all()
    form = ColaboradorForm()
    context = {'form': form, "cargos": cargos}
    return render(request, "colaboradores/create.html", context)


@login_required
def store(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            colaborador = Colaborador()
            colaborador.nome = request.POST['nome']
            colaborador.data_nascimento = datetime.strptime(request.POST['data_nascimento'], "%d/%m/%Y").strftime('%Y-%m-%d')
            colaborador.cpf = request.POST['cpf']
            colaborador.rg = request.POST['rg']
            colaborador.email = request.POST['email']
            colaborador.telefone = request.POST['telefone']
            colaborador.endereco = request.POST['endereco']
            colaborador.numero = request.POST['numero']
            colaborador.complemento = request.POST['complemento']
            colaborador.cidade = request.POST['cidade']
            colaborador.bairro = request.POST['bairro']
            colaborador.estado = request.POST['estado']
            colaborador.observacoes = request.POST['observacoes']
            messages.success(request, "Colaborador Cadastrado com Sucesso!")
            colaborador.save()
            return redirect(reverse('colaboradores_home'))


@login_required
def edit(request, colaborador_id):
    colaborador = get_object_or_404(Colaborador, pk=colaborador_id)
    initial_form = {
        "nome": colaborador.nome,
        "data_nascimento": colaborador.data_nascimento,
        "cpf": colaborador.cpf,
        "rg": colaborador.rg,
        "email": colaborador.email,
        "telefone": colaborador.telefone,
        "endereco": colaborador.endereco,
        "numero": colaborador.numero,
        "complemento": colaborador.complemento,
        "cidade": colaborador.cidade,
        "bairro": colaborador.bairro,
        "estado": colaborador.estado,
        "observacoes": colaborador.observacoes,
    }
    form = ColaboradorForm(initial=initial_form)
    context = {"colaborador": colaborador, 'form': form}
    return render(request, "colaboradores/edit.html", context)


@login_required
def update(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            colaborador = Colaborador.objects.get(pk=request.POST['id_colaborador'])
            colaborador.nome = request.POST['nome']
            colaborador.data_nascimento = request.POST['data_nascimento']
            colaborador.cpf = request.POST['cpf']
            colaborador.rg = request.POST['rg']
            colaborador.email = request.POST['email']
            colaborador.telefone = request.POST['telefone']
            colaborador.endereco = request.POST['endereco']
            colaborador.numero = request.POST['numero']
            colaborador.complemento = request.POST['complemento']
            colaborador.cidade = request.POST['cidade']
            colaborador.bairro = request.POST['bairro']
            colaborador.estado = request.POST['estado']
            colaborador.observacoes = request.POST['observacoes']
            colaborador.save()
            messages.success(request, "Colaborador Atualizado com Sucesso!")
            return redirect(reverse('colaboradores_home'))


@login_required
def delete(request, colaborador_id):
    colaborador = get_object_or_404(Colaborador, pk=colaborador_id)
    colaborador.delete()
    messages.success(request, "Colaborador Excluído com Sucesso!")
    return redirect(reverse('colaboradores_home'))
