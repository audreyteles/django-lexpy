import os
from django.apps import AppConfig

from django_lexpy.commands import lexpy


class LexpyConfig(AppConfig):
    name = "django_lexpy"
    verbose_name = "django-lexpy"
    dir_project = os.getcwd()

    def ready(self):
        lexpy.main()
