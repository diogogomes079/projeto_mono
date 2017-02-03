# coding=utf-8
from django.contrib import admin
from catalogoresgd.catalogo.models import Profissao, Profissional

class ProfissaoModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}
    list_display = ['nome', 'slug', 'criado_em', 'modificado_em']
    search_fields = ['nome', 'slug']
    list_filter = ['criado_em', 'modificado_em']


class ProfissionalModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}
    list_display = ['nome', 'idade', 'sexo', 'experiencia', 'fone', 'email', 'cpf', 'criado_em', 'modificado_em']
    search_fields = ['nome', 'experiencia']
    list_filter = ['criado_em', 'modificado_em']


admin.site.register(Profissao, ProfissaoModelAdmin)
admin.site.register(Profissional, ProfissionalModelAdmin)