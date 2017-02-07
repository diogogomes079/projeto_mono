#coding=utf-8

from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        mensagem = self.cleaned_data['mensagem']
        mensagem = 'Nome: {0}\nE-mail: {1}\nMensagem: {2}'.format(nome, email, mensagem)
        send_mail('Contato do Catalogo RESGD',
              mensagem,
              settings.DEFAULT_FROM_EMAIL,
              [settings.DEFAULT_FROM_EMAIL, email]
              )

    '''
        def __init__(self, *args, **kwargs):
            super(ContatoForm, self).__init__(*args, **kwargs)
            self.fields['nome'].widget.attrs['class'] = 'form-control'
            self.fields['email'].widget.attrs['class'] = 'form-control'
            self.fields['mensagem'].widget.attrs['class'] = 'form-control'
    '''