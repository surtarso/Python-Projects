# Generated by Django 4.0.5 on 2022-06-27 11:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0029_carteiraativos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarteiraAtivos',
            new_name='CarteiraAtivo',
        ),
    ]
