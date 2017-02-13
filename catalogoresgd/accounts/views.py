# coding=utf-8

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, FormView

from .forms import UsuarioAdminCreationForm
from .models import Usuario


class IndexContaView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/conta_usuario.html'


class RegistroView(CreateView):
    model = Usuario
    template_name = 'accounts/cadastrar_usuario.html'
    form_class = UsuarioAdminCreationForm
    success_url = reverse_lazy('home')


class AtualizarUsuarioView(LoginRequiredMixin, UpdateView):

    model = Usuario
    template_name = 'accounts/atualizar_usuario.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('conta:index_conta')

    def get_object(self):
        return self.request.user


class AtualizarSenhaView(LoginRequiredMixin, FormView):

    template_name = 'accounts/atualizar_senha.html'
    success_url = reverse_lazy('conta:index_conta')
    form_class = PasswordChangeForm
    def get_form_kwargs(self):
        kwarg = super(AtualizarSenhaView, self).get_form_kwargs()
        kwarg['user'] = self.request.user
        return kwarg

index_conta = IndexContaView.as_view()
registrar_usuario = RegistroView.as_view()
atualizar_usuario = AtualizarUsuarioView.as_view()
atualizar_senha = AtualizarSenhaView.as_view()