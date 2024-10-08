import importlib

import rich
from django import template

from django.conf import settings

register = template.Library()

# Get language code from settings
language_settings = settings.LANGUAGE_CODE.replace("-", "_")

lang_module = importlib.import_module(f'lang.{language_settings}')
messages = lang_module.messages


@register.simple_tag
def lexpy(message):
    command = message.split(".")

    assert len(command) == 2, "Your call are wrong, try something like 'message.welcome'"

    prefix, content = command[0], command[1]

    assert prefix == "message", f"The prefix '{prefix}' isn't allowed, try something like 'message._____'"

    assert message in messages, "This message don't exists!"

    return messages.get(message)
