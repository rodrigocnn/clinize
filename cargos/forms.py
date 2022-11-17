
from django import forms


class CargoForm(forms.Form):

    descricao = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
