from django import forms
from .models import Client, Teacher


class ClientForm(forms.Form):
    class Meta:
        model = Client
        fields = ["Login", "Password"]

    login = forms.CharField()
    password = forms.PasswordInput()
