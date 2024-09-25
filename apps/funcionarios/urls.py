from django.urls import path
from apps.funcionarios.views import cadastro_funcionarios, lista_funcionarios

urlpatterns = [
    path('lista_funcionarios/', lista_funcionarios, name='lista_funcionarios'),
    path('cadastro_funcionario/', cadastro_funcionarios, name='cadastro_funcionario'),
]