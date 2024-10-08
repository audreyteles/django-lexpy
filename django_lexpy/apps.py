import os
from pathlib import Path

from django.apps import AppConfig


class LexpyConfig(AppConfig):
    name = "django_lexpy"
    label = "lexpy"

    def __init__(self):
        self.dir_project = os.getcwd()

    def get(self):
        return self.dir_project
