# Generated by Django 4.0.5 on 2022-06-17 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_alter_alerta_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ativo',
            name='ticker',
            field=models.CharField(default='CHOOSE', max_length=30),
        ),
    ]