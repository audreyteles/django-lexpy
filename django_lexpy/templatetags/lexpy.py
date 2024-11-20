from django import template

from django_lexpy.templatetags.utils import ShortKey

register = template.Library()


@register.simple_tag
def lexpy(short_key: str, *args, **kwargs):
    return ShortKey(short_key).args(*args, **kwargs)
