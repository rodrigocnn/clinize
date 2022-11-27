from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime
from django.contrib import messages
from agenda.forms import AgendaForm
from agenda.models import Agenda


def index(request):
    return render(request, "agendas/index.html")


def events(request):
    # eventos = Paciente.objects.all()
    return render(request, "agendas/index.html")


def create(request):
    return render(request, "agendas/create.html")


def store(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        start = request.POST['data_evento'] + " " + request.POST['hora_inicio']
        end = request.POST['data_evento'] + " " + request.POST['hora_fim']
        if form.is_valid():
            agenda = Agenda()
            agenda.title = request.POST['descricao']
            agenda.start = datetime.strptime(start, "%d/%m/%Y %H:%M").strftime('%Y-%m-%dT%H:%M:%SZ')
            agenda.end = datetime.strptime(end, "%d/%m/%Y %H:%M").strftime('%Y-%m-%dT%H:%M:%SZ')
            messages.success(request, "Agenda Cadastrada com Sucesso!")
            agenda.save()

    return redirect(reverse('agenda_home'))
