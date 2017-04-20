from django import template

register = template.Library()

@register.filter(name="str_add")
def str_add(value, arg, *args):
    value += str(arg)
    for a in args:
        value += str(a)
    return value