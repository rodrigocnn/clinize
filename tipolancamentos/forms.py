
from django import forms


class TipoLancamentoForm(forms.Form):
    descricao = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
