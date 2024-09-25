# apps/funcionarios/forms.py
from django import forms

class FuncionarioForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='Nome')
    last_name = forms.CharField(max_length=100, label='Sobrenome')
    email = forms.EmailField(label='Email')
    cargo = forms.CharField(max_length=100, label='Cargo')
    username = forms.CharField(max_length=100, label='Nome de Usuário')
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
