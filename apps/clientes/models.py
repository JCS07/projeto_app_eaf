from django.db import models
from datetime import datetime

class Clientes(models.Model):

    OPCOES_DOCUMENTOS = [
        ('RG','RG'),
        ('CPF','CPF'),
        ('CNH', 'CPF'),
    ]

    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    contact = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField()
    born_date = models.DateTimeField(null=False, blank=False)
    document_type = models.CharField(max_length=100, choices=OPCOES_DOCUMENTOS, default='')
    document = models.CharField(max_length=20, null=False, blank=False)
    contact_date = models.DateTimeField(default=datetime.now, null=False, blank=False)

    def __str__(self):
        return self.first_name