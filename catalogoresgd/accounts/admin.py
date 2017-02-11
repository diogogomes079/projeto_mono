# coding=utf-8

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario
from .forms import UsuarioAdminCreationForm, UsuarioAdminForm


class UsuarioAdmin(BaseUserAdmin):

    add_form = UsuarioAdminCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('username','name', 'email', 'password1', 'password2')
        }),
    )
    form = UsuarioAdminForm
    fieldsets = (
        (None, {
            'fields': ('username', 'email')
        }),
        ('Informações Básicas', {
            'fields': ('name', 'last_login')
        }),
        (
            'Permissões', {
                'fields': (
                    'is_active', 'is_staff', 'is_superuser', 'groups',
                    'user_permissions'
                )
            }
        ),
    )
    list_display = ['username', 'name', 'email', 'is_active', 'is_staff', 'date_joined']


admin.site.register(Usuario, UsuarioAdmin)
