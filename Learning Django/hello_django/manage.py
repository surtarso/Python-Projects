#!/usr/bin/env python

## wrapper do django-admin.py!
## delega as acoes pro admin e procura o PATH
## define a django_setting_model settings.py
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    ##onde estao as configuracoes pro proj ser executado
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    ## coloca o pacote dentro do sys
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
