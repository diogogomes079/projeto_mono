# coding=utf-8

from django.conf.urls import url, include
from django.contrib import admin

from catalogoresgd.core.views import *
from catalogoresgd.catalogo.views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^sobre/$', sobre, name='sobre'),
    url(r'^contato/$', contato, name='contato'),
    url(r'^catalogo/', include('catalogoresgd.catalogo.urls',
                               namespace='catalogo')),

    url(r'^admin/', admin.site.urls),
]
