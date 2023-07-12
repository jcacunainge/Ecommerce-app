from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # Campos pre-populados basados en otros campos
    prepopulated_fields = {'slug': ('category_name',)}

    # Campos que se mostrarán en la lista de objetos en el panel de administración
    list_display = ('category_name', 'slug')


admin.site.register(Category, CategoryAdmin)
