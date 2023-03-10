# Generated by Django 4.1.3 on 2022-12-03 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('colaboradores', '0001_initial'),
        ('pacientes', '0001_initial'),
        ('procedimentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colaboradores.colaborador')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente')),
                ('procedimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procedimentos.procedimento')),
            ],
        ),
    ]
