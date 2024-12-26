from django import template

register = template.Library()

@register.filter
def attr(field, arg):
    if not hasattr(field, 'as_widget'):
        raise ValueError("Expected a form field, got: {}".format(type(field)))
    return field.as_widget(attrs={arg: True})

