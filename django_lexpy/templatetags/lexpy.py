from django import template

from django_lexpy.templatetags.utils import ShortKey

register = template.Library()


@register.simple_tag
def lexpy(short_key: str):
    return ShortKey(short_key).message
