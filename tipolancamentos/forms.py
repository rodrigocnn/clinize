
# from django import forms
from django.forms import ModelForm

from tipolancamentos.models import TipoLancamento


class TipoLancamentoForm(ModelForm):
    class Meta:
        model = TipoLancamento
        fields = ['descricao', 'tipo']
