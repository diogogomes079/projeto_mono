# coding=utf-8

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout
from catalogoresgd.core.views import *
from catalogoresgd.catalogo.views import *
from catalogoresgd.accounts.views import *

urlpatterns = [

    url(r'^$', index, name='home'),
    url(r'^sobre/$', sobre, name='sobre'),
    url(r'^contato/$', contato, name='contato'),

    # URL APP's
    url(r'^catalogo/', include('catalogoresgd.catalogo.urls', namespace='catalogo')),
    url(r'^conta/', include('catalogoresgd.accounts.urls', namespace='conta')),

    # URL AUTH
    url(r'^entrar/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'home'}, name='logout'),

    # URL ADMIN
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    #ou -> urlpatterns += static(
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
