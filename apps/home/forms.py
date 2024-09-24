#importação do FORMS
from django import forms

#classe para LOGIN
class LoginForms (forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Maria Silva',
            }
        )
    )
    senha_login=forms.CharField(
        label='Senha',
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )