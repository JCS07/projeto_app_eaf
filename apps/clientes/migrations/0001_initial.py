# Generated by Django 5.1.1 on 2024-09-25 22:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroClientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('born_date', models.DateTimeField()),
                ('document_type', models.CharField(choices=[('RG', 'RG'), ('CPF', 'CPF'), ('CNH', 'CPF')], default='', max_length=100)),
                ('document', models.CharField(max_length=20)),
                ('contact_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
