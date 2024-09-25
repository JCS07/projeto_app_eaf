from django.shortcuts import render
from apps.clientes.models import Clientes

def lista_clientes(request):
    clientes = Clientes.objects.all()  # Busca todos os funcionários
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

from django.shortcuts import render, redirect
from apps.clientes.forms import CadastroClientes
from apps.clientes.models import Clientes

def cadastro_clientes(request):
    if request.method == 'POST':
        form = CadastroClientes(request.POST)
        if form.is_valid():
            # Cria um novo cliente a partir do formulário
            Clientes.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                contact=form.cleaned_data['contact'],
                email=form.cleaned_data['email'],
                born_date=form.cleaned_data['born_date'],
                document_type=form.cleaned_data['document_type'],
                document=form.cleaned_data['document'],
                contact_date=form.cleaned_data['contact_date'],
            )
            return redirect('lista_clientes')  # Redireciona após o cadastro bem-sucedido
    else:
        form = CadastroClientes()
    
    return render(request, 'clientes/cadastro_clientes.html', {'form': form})
