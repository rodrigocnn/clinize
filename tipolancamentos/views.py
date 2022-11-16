from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from tipolancamentos.forms import TipoLancamentoForm
from tipolancamentos.models import TipoLancamento


def index(request):
    lancamentos = TipoLancamento.objects.all()
    return render(request, "tipolancamentos/index.html", context={"lancamentos": lancamentos})


def create(request):
    return render(request=request, template_name="tipolancamentos/create.html")


def store(request):
    if request.method == 'POST':
        form = TipoLancamentoForm(request.POST)
        if form.is_valid():
            lancamento = TipoLancamento()
            lancamento.descricao = request.POST['descricao']
            lancamento.tipo = request.POST['tipo']
            messages.success(request, "Lançamento Cadastrado com Sucesso!")
            lancamento.save()

    return redirect(reverse('tipo_lancamento_home'))


def edit(request, lancamento_id):
    lancamento = get_object_or_404(TipoLancamento, pk=lancamento_id)
    initial_form = {
        "descricao": lancamento.descricao,
        "tipo": lancamento.tipo,

    }
    form = TipoLancamentoForm(initial=initial_form)
    context = {"lancamento": lancamento, 'form': form}
    return render(request, "tipolancamentos/edit.html", context)


def update(request):
    if request.method == 'POST':
        form = TipoLancamentoForm(request.POST)
        if form.is_valid():
            lancamento = TipoLancamento.objects.get(pk=request.POST['id_lancamento'])
            lancamento.descricao = request.POST['descricao']
            lancamento.tipo = request.POST['tipo']
            messages.success(request, "Tipo de Lançamento Atualizado com Sucesso!")
            lancamento.save()
            return redirect(reverse('tipo_lancamento_home'))


def delete(request, lancamento_id):
    lancamento = get_object_or_404(TipoLancamento, pk=lancamento_id)
    lancamento.delete()
    messages.success(request, "Tipo de Lancamento Excluído com Sucesso!")
    return redirect(reverse('tipo_lancamento_home'))
