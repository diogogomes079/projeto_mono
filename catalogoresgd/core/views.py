from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContatoForm


class IndexView(TemplateView):
    template_name = 'index.html'


def sobre(request):
    return render(request, 'sobre.html')

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