# coding=utf-8

from django.conf.urls import url
from .views import *


urlpatterns =[
    url(r'^$', index_conta, name='index_conta'),
    url(r'^registro/$', registrar_usuario, name='registrar_user'),
    url(r'^alterar-dados/$', atualizar_usuario, name='atualizar_user'),
    url(r'^alterar-senha/$', atualizar_senha, name='atualizar_password'),

]