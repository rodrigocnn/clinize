# Generated by Django 4.1.3 on 2022-11-17 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cargos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.CharField(blank=True, max_length=20)),
                ('rg', models.CharField(max_length=20)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('observacoes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cargo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cargos.cargo')),
            ],
        ),
    ]
