
from django import forms


class PacienteForm(forms.Form):
    ATTRS_DATA = {'class': 'form-control datepicker', 'autocomplete': 'off'}
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_nascimento = forms.CharField(max_length=20, widget=forms.TextInput(attrs=ATTRS_DATA))
    cpf = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    rg = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': 'form-control'}))
    endereco = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    numero = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    complemento = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cidade = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    bairro = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    estado = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    observacoes = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 5, 'class': 'form-control'}))
