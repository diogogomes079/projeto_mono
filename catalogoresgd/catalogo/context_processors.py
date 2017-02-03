# coding=utf-8
from .models import Profissao


def listar_profissoes_no_catalogo(request):
    return {
        'listar_profissoes': Profissao.objects.all()
    }