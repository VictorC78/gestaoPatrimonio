# Generated by Django 5.1.4 on 2025-02-17 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_departamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('numero_tombamento', models.CharField(max_length=50, unique=True)),
                ('tagRFID', models.CharField(max_length=50, unique=True)),
                ('data_aquisicao', models.DateField()),
                ('valor_aquisicao', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado_conservacao', models.CharField(choices=[('novo', 'Novo'), ('usado', 'Usado'), ('danificado', 'Danificado'), ('inservivel', 'Inservível')], max_length=50)),
                ('situacao', models.CharField(choices=[('ativo', 'Ativo'), ('baixado', 'Baixado'), ('emprestado', 'Emprestado')], max_length=50)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categoria')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.departamento')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.fornecedor')),
            ],
        ),
    ]
