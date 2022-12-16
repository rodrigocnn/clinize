
from django import forms


class ProcedimentoForm(forms.Form):
    ATTRS_DATA = {'class': 'form-control datepicker', 'autocomplete': 'off'}
    descricao = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.DecimalField(max_digits=6, decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
