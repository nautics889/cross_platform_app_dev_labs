#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from utils import logger


def main():
    settings_file = 'sandbox.settings'
    if os.environ.get('MODE') == 'DEV':
        logger.info('Running service in a development mode...')
        settings_file = 'sandbox.settings_dev'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_file)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
