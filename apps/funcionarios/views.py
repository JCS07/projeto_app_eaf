from django.shortcuts import render, redirect
from .models import Funcionario
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import FuncionarioForm

def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()  # Busca todos os funcionários
    return render(request, 'funcionarios/lista_funcionarios.html', {'funcionarios': funcionarios})

def cadastro_funcionarios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cargo = request.POST.get('cargo')
        data_contratacao = request.POST.get('data_contratacao')

        # Cria o usuário
        user = User.objects.create_user(username=email, email=email, password=senha)
        user.first_name = nome
        user.last_name = sobrenome
        user.save()

        # Cria o funcionário
        Funcionario.objects.create(user=user, first_name=nome, last_name=sobrenome, email=email, cargo=cargo, data_contratacao=data_contratacao)

        # Faz login automático
        messages.success(request, 'Funcionário cadastrado com sucesso!')
        return redirect('lista_funcionarios')  # Redireciona para a lista de funcionários ou outra página

    return render(request, 'funcionarios/cadastro_funcionario.html')