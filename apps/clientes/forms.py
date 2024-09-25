from django import forms
from apps.clientes.models import Clientes

class CadastroClientes(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'contact': 'Contato',
            'email': 'E-mail',
            'born_date': 'Data de nascimento',
            'document_type': 'Tipo do documento',
            'document': 'Num. do documento',
            'contact_date': 'Data de contato',
        }