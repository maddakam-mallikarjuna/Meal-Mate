from django import template

register = template.Library()

@register.filter
def split_string(value, delimiter=","):
    """Splits a string by the given delimiter and returns a list."""
    return value.split(delimiter) if value else []
