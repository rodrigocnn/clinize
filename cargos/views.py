from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse


from cargos.forms import CargoForm
from cargos.models import Cargo


def index(request):
    cargos = Cargo.objects.all()
    return render(request, "cargos/index.html", context={"cargos":  cargos})


def create(request):
    return render(request=request, template_name="cargos/create.html")


def store(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            cargo = Cargo()
            cargo.descricao = request.POST['descricao']
            messages.success(request, "Cargo Cadastrado com Sucesso!")
            cargo.save()

    return redirect(reverse('cargos_home'))


def edit(request, cargo_id):
    cargo = get_object_or_404(Cargo, pk=cargo_id)
    initial_form = {"descricao": cargo.descricao}
    form = CargoForm(initial=initial_form)
    context = {"cargo": cargo, 'form': form}
    return render(request, "cargos/edit.html", context)


def update(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            cargo = Cargo.objects.get(pk=request.POST['id_cargo'])
            cargo.descricao = request.POST['descricao']
            messages.success(request, "Cargo Atualizado com Sucesso!")
            cargo.save()

    return redirect(reverse('cargos_home'))


def delete(request, cargo_id):
    cargo = get_object_or_404(Cargo, pk=cargo_id)
    cargo.delete()
    messages.success(request, "Cargo Excluído com Sucesso!")
    return redirect(reverse('cargos_home'))
