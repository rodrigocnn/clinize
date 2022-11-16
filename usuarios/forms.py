
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
