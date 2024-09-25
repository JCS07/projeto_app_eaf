from django.shortcuts import render, redirect
from apps.home.forms import LoginForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def home_view(request):
    return render(request, 'home/index.html')

def login_view(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha_login'].value()
        
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('menu_geral')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')

    return render(request, 'home/login.html', {'form': form})