# Generated by Django 4.0.5 on 2022-06-17 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_delete_ativo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alerta',
            name='ativo',
        ),
    ]
