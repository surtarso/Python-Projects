# Generated by Django 4.0.5 on 2022-06-15 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_pedido_precovenda'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='precocompra',
            field=models.DecimalField(decimal_places=2, default=0.01, max_digits=6),
        ),
    ]
