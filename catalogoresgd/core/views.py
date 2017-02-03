from django.shortcuts import render
from django.views.generic import TemplateView, View


class IndexView(TemplateView):
    template_name = 'index.html'


def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')


index = IndexView.as_view()