from django import template
import hashlib

register = template.Library()

@register.filter(name="str_add")
def str_add(value, arg, *args):
    value = str(value)
    value += str(arg)
    for a in args:
        value += str(a)
    return value

@register.filter(name='md5')
def md5_string(value):
    return hashlib.md5(value.encode(encoding='UTF-8')).hexdigest()
