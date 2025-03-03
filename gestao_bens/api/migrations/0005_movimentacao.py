# Generated by Django 5.1.4 on 2025-02-17 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_bem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_movimentacao', models.CharField(choices=[('transferencia', 'Transferência'), ('baixa', 'Baixa'), ('manutencao', 'Manutenção'), ('emprestimo', 'Empréstimo')], max_length=50)),
                ('data_movimentacao', models.DateTimeField(auto_now_add=True)),
                ('justificativa', models.TextField()),
                ('bem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bem')),
                ('destino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destino', to='api.departamento')),
                ('origem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origem', to='api.departamento')),
            ],
        ),
    ]
