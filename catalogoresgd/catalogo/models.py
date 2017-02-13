# coding=utf-8

from django.db import models
from .choices import SEXO
from django.core.urlresolvers import reverse


class Profissao(models.Model):

    nome = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    modificado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Profissão'
        verbose_name_plural = 'Profissões'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('catalogo:profissao', kwargs={'slug': self.slug})

class Profissional(models.Model):

    nome = models.CharField('Nome', max_length=200)
    slug = models.SlugField('Identigicador', max_length=200)
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('E-mail', blank=True)
    fone = models.CharField('Telefone', max_length=20)
    idade = models.CharField('Idade', max_length=3)
    experiencia = models.CharField("Experiência", max_length=2)
    profissao = models.ManyToManyField('Profissao', verbose_name='Profissão')
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO)
    imagem = models.ImageField('Imagem', upload_to='profissionais', blank=True, null=True)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    modificado_em = models.DateTimeField('Atualizado em', auto_now=True)


    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('catalogo:perfil_profissional', kwargs={'slug': self.slug})