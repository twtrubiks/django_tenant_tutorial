from django.contrib import admin

from customers.models import Client, Domain
from django_tenants.admin import TenantAdminMixin

class DomainInline(admin.TabularInline):
    model = Domain


# # https://django-tenants.readthedocs.io/en/latest/install.html#admin-support
# @admin.register(Client)
# class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
#     inlines = [DomainInline]
#     list_display = ('schema_name', 'name')


@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    inlines = [DomainInline]
    list_display = ('schema_name', 'name')
