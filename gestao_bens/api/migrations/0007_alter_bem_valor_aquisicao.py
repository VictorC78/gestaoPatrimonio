# Generated by Django 5.1.4 on 2025-02-22 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_bem_qnt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bem',
            name='valor_aquisicao',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
