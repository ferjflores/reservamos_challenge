import os
import sys
import django
from django.conf import settings


def django_command(command):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weather_api.settings")
    django.setup()
    from django.core.management import execute_from_command_line
    execute_from_command_line([sys.argv[0]] + command.split())


def runserver():
    django_command("runserver")


def test():
    django_command("test")


def test_unit():
    django_command("test tests.unit")


def test_integration():
    django_command("test tests.integration")


def makemigrations():
    django_command("makemigrations")


def migrate():
    django_command("migrate")


def showmigrations():
    django_command("showmigrations")


if __name__ == "__main__":
    globals()[sys.argv[1]]()
