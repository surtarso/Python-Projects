# Generated by Django 4.0.5 on 2022-06-27 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0034_remove_carteiraativo_user_carteiraativo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ativo',
            name='user',
        ),
        migrations.AlterField(
            model_name='ativo',
            name='ticker',
            field=models.CharField(default='CHOOSE/ADD', max_length=30),
        ),
    ]
