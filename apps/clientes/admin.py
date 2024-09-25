from django.contrib import admin
from .models import Clientes  # Importa o modelo Clientes

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact', 'email', 'born_date', 'document_type', 'document', 'contact_date')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('document_type',)  # Permite filtrar por tipo de documento

admin.site.register(Clientes, ClientesAdmin)  # Registra o modelo com a classe de administração