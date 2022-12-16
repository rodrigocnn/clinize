
from django import forms


class AgendaForm(forms.Form):
    ATTRS_DATA = {'class': 'form-control datepicker', 'autocomplete': 'off'}

    paciente_id = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    colaborador_id = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    procedimento_id = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_evento = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    hora_inicio = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    hora_fim = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
