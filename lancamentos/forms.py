
from django import forms


class LancamentoForm(forms.Form):
    data = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_lancamento = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    classificacao = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    observacoes = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 5, 'class': 'form-control'}))
