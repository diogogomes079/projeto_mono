# coding=utf-8

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario

class UsuarioAdminCreationForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ['username', 'name', 'email']


class UsuarioAdminForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['username', 'name', 'email', 'is_active', 'is_staff']
