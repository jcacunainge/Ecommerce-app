from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    # Campos que se mostrarán en la lista de objetos en el panel de administración
    list_display = ('email', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active')

    # Campos en la lista de objetos que serán enlaces clicables para acceder al detalle completo de cada objeto
    list_display_links = ('email', 'first_name', 'last_name')

    # Campos que se mostrarán como solo lectura en el formulario de edición del objeto
    readonly_fields = ('last_login', 'date_joined')

    # Orden en el que se mostrarán los objetos en la lista (en orden descendente de fecha de unión)
    ordering = ('-date_joined',)

    # Campos de muchos a muchos que se mostrarán como una interfaz de selección horizontal
    filter_horizontal = ()

    # Campos por los que se puede filtrar la lista de objetos
    list_filter = ()

    # Conjuntos de campos que se mostrarán en el formulario de edición del objeto
    fieldsets = ()



# Register your models here.
admin.site.register(Account, AccountAdmin)
