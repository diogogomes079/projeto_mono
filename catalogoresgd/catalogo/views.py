from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *


class ProfissionaisListView(generic.ListView):

    model = Profissional
    template_name = 'catalogo/listar_profissionais.html'
    context_object_name = 'listar_profissionais'
    paginate_by = 4


class ProfissaoListView(generic.ListView):

    template_name = 'catalogo/profissao.html'
    context_object_name = 'listar_profissionais'
    paginate_by = 4

    def get_queryset(self):
        return Profissional.objects.filter(profissao__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(ProfissaoListView, self).get_context_data(**kwargs)
        context['profissao_atual'] = get_object_or_404(Profissao, slug=self.kwargs['slug'])
        return context


def perfil_profissional(request, slug):
    perfil = Profissional.objects.get(slug=slug)
    context = {
        'perfil_profissional': perfil
    }
    return render(request, 'catalogo/perfil_profissional.html', context)


profissionais = ProfissionaisListView.as_view()
profissao = ProfissaoListView.as_view()