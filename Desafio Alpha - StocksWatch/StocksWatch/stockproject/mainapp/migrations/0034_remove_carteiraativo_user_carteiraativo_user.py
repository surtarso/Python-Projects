# Generated by Django 4.0.5 on 2022-06-27 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0033_remove_carteiraativo_preco_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carteiraativo',
            name='user',
        ),
        migrations.AddField(
            model_name='carteiraativo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
