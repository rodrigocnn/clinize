from datetime import datetime
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from pacientes.models import Paciente
from pacientes.forms import PacienteForm


@login_required
def index(request):
    pacientes = Paciente.objects.all()
    return render(request, "pacientes/index.html", context={"pacientes": pacientes})


@login_required
def create(request):
    form = PacienteForm()
    context = {'form': form}
    return render(request, "pacientes/create.html", context)


@login_required
def store(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = Paciente()
            paciente.nome = request.POST['nome']
            paciente.data_nascimento = datetime.strptime(request.POST['data_nascimento'], "%d/%m/%Y").strftime('%Y-%m-%d')
            paciente.cpf = request.POST['cpf']
            paciente.rg = request.POST['rg']
            paciente.email = request.POST['email']
            paciente.telefone = request.POST['telefone']
            paciente.endereco = request.POST['endereco']
            paciente.numero = request.POST['numero']
            paciente.complemento = request.POST['complemento']
            paciente.cidade = request.POST['cidade']
            paciente.bairro = request.POST['bairro']
            paciente.estado = request.POST['estado']
            paciente.observacoes = request.POST['observacoes']
            messages.success(request, "Paciente Cadastrado com Sucesso!")
            paciente.save()
            return redirect('/pacientes/')


@login_required
def edit(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    initial_form = {
        "nome": paciente.nome,
        "data_nascimento": paciente.data_nascimento,
        "cpf": paciente.cpf,
        "rg": paciente.rg,
        "email": paciente.email,
        "telefone": paciente.telefone,
        "endereco": paciente.endereco,
        "numero": paciente.numero,
        "complemento": paciente.complemento,
        "cidade": paciente.cidade,
        "bairro": paciente.bairro,
        "estado": paciente.estado,
        "observacoes": paciente.observacoes,
    }
    form = PacienteForm(initial=initial_form)
    context = {"paciente": paciente, 'form': form}
    return render(request, "pacientes/edit.html", context)


@login_required
def update(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = Paciente.objects.get(pk=request.POST['id_paciente'])
            paciente.nome = request.POST['nome']
            paciente.data_nascimento = request.POST['data_nascimento']
            paciente.cpf = request.POST['cpf']
            paciente.rg = request.POST['rg']
            paciente.email = request.POST['email']
            paciente.telefone = request.POST['telefone']
            paciente.endereco = request.POST['endereco']
            paciente.numero = request.POST['numero']
            paciente.complemento = request.POST['complemento']
            paciente.cidade = request.POST['cidade']
            paciente.bairro = request.POST['bairro']
            paciente.estado = request.POST['estado']
            paciente.observacoes = request.POST['observacoes']
            paciente.save()
            messages.success(request, "Paciente Atualizado com Sucesso!")
            return redirect('/pacientes/')


@login_required
def delete(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    paciente.delete()
    messages.success(request, "Paciente Excluído com Sucesso!")
    return redirect('/pacientes/')
