from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import ContatoForm


class IndexView(TemplateView):
    template_name = 'index.html'


class SobreView(TemplateView):
    template_name = 'sobre.html'


def contato(request):
    sucesso = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        sucesso = True
    context = {
        'form': form,
        'sucesso': sucesso,
    }
    return render(request, 'contato.html', context)


index = IndexView.as_view()
sobre = SobreView.as_view()