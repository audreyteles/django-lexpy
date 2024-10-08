import os
import rich
import typer
import shutil
import django
from django.conf import settings
from django_lexpy.apps import LexpyConfig

app = typer.Typer()
settings.configure()

@app.command()
def main():
    config = LexpyConfig()

    rich.print("[green]Initializing lexpy...[/green]")

    # if the parameter is not given, get the LANGUAGE_CODE from settings.py
    language = settings.LANGUAGE_CODE.replace("-", "_")

    # Store path to a specific folder messages
    base_dir = os.path.join(config.get(), 'lang', language)

    if not os.path.exists(base_dir):

        # Make directories
        os.makedirs(base_dir, exist_ok=True)

        # Copy sample files to the chosen folder
        try:
            local_path = os.path.dirname(os.path.realpath(__file__))
            sample_files = os.path.join(local_path, 'sample_files')

            shutil.copyfile(os.path.join(sample_files,'init_sample'),  os.path.join(base_dir, '__init__.py'))
            shutil.copyfile(os.path.join(sample_files,'messages_sample'), os.path.join(base_dir, 'main.py'))
        except FileNotFoundError:
            rich.print("[red]Files not found to copy...[/red]")

    rich.print("[green]Done![/green]")


if __name__ == "__main__":
    app()
