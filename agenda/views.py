import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.core.serializers import serialize
from datetime import datetime
from django.contrib import messages
from agenda.forms import AgendaForm
from agenda.models import Agenda
from procedimentos.models import Procedimento
from pacientes.models import Paciente
from colaboradores.models import Colaborador


def index(request):
    return render(request, "agendas/index.html")


def events(request):
    eventos_queryset = Agenda.objects.all()
    data_serielize = serialize('json', eventos_queryset, fields=('title', 'start', 'end'))
    data = json.loads(data_serielize)
    eventos = []
    for item in data:
        eventos.append({
            "id": item['pk'],
            "title": item['fields']['title'],
            "start": item['fields']['start'],
            "end": item['fields']['start']
            })

    return JsonResponse(eventos, safe=False)


def create(request):
    procedimentos = Procedimento.objects.all()
    pacientes = Paciente.objects.all()
    colaboradores = Colaborador.objects.all()
    context = {"procedimentos":  procedimentos, "pacientes": pacientes, "colaboradores": colaboradores}
    return render(request=request, template_name="agendas/create.html", context=context)


def store(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        start = request.POST['data_evento'] + " " + request.POST['hora_inicio']
        end = request.POST['data_evento'] + " " + request.POST['hora_fim']
        paciente = Paciente.objects.get(id=int(request.POST['paciente_id']))
        colaborador = Colaborador.objects.get(id=int(request.POST['colaborador_id']))
        procedimento = Procedimento.objects.get(id=int(request.POST['procedimento_id']))
        if form.is_valid():
            agenda = Agenda()
            agenda.title = colaborador.nome
            agenda.start = datetime.strptime(start, "%d/%m/%Y %H:%M").strftime('%Y-%m-%dT%H:%M:%SZ')
            agenda.end = datetime.strptime(end, "%d/%m/%Y %H:%M").strftime('%Y-%m-%dT%H:%M:%SZ')
            agenda.colaborador = colaborador
            agenda.paciente = paciente
            agenda.procedimento = procedimento
            messages.success(request, "Agenda Cadastrada com Sucesso!")
            agenda.save()

    return redirect(reverse('agenda_home'))
