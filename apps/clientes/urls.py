from django.urls import path
from apps.clientes.views import cadastro_clientes, lista_clientes

urlpatterns = [
    path('lista_clientes/', lista_clientes, name='lista_clientes'),
    path('cadastro_clientes/', cadastro_clientes, name='cadastro_clientes'),
]