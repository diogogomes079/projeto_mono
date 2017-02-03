from django.shortcuts import render
from .models import *


def profissionais(request):
    listar_profissionais = Profissional.objects.all()
    context={
        'listar_profissionais': listar_profissionais,
    }
    return render(request, 'catalogo/listar_profissionais.html', context)


def profissao(request, slug):
    profissao_atual = Profissao.objects.get(slug=slug)
    profissional = Profissional.objects.filter(profissao=profissao_atual)
    context = {
        'profissao_atual': profissao_atual,
        'listar_profissionais': profissional,
    }
    return render(request, 'catalogo/profissao.html', context)


def perfil_profissional(request, slug):
    perfil = Profissional.objects.get(slug=slug)
    context = {
        'perfil_profissional': perfil
    }
    return render(request, 'catalogo/perfil_profissional.html', context)
