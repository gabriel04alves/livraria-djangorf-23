# Generated by Django 5.1.1 on 2024-10-08 18:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0005_itenscompra_preco_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
