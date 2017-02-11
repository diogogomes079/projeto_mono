# coding=utf-8

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from catalogoresgd.core.views import *
from catalogoresgd.catalogo.views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^sobre/$', sobre, name='sobre'),
    url(r'^contato/$', contato, name='contato'),
    url(r'^catalogo/', include('catalogoresgd.catalogo.urls', namespace='catalogo')),


    url(r'^entrar/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'home'}, name='logout'),
    url(r'^registro/$', resgistar_user, name='registrar_user'),
    url(r'^admin/', admin.site.urls),
]
