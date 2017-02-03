# coding=utf-8

from django.conf.urls import url
from .views import *


urlpatterns =[
    url(r'^profissionais/$', profissionais, name='profissionais'),
    url(r'^profissional/(?P<slug>[\w_-]+)/$', perfil_profissional, name='perfil_profissional'),
    url(r'^(?P<slug>[\w_-]+)/$', profissao, name='profissao'),

]