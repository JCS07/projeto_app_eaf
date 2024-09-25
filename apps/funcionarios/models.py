from django.db import models
from django.contrib.auth.models import User

class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, null=True, blank=True)  # Permite nulo
    cargo = models.CharField(max_length=50)
    data_contratacao = models.DateField()

    def __str__(self):
        return self.first_name
